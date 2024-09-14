from flask_restful import Resource, request, reqparse, abort
from flask_restful import fields, marshal, marshal_with
from .model import City
from settings import db

city_fields = {
    'id': fields.Integer,
    'name': fields.String
}

city_list_fields = {
    'total': fields.Integer,
    'cities': fields.List(fields.Nested(city_fields))
}

args_parser = reqparse.RequestParser()
args_parser.add_argument('id', type=int, help="City id should be integer")
args_parser.add_argument('name', type=str, required=True, help="City name cannot be empty")

class CityResource(Resource):
    def get(self, city_id = None):
        if city_id:
            city = City.query.get_or_404(city_id, description = "No cities found matching the criteria")
            return marshal(City, city_fields)
        else:
            request_args = request.args.to_dict()
            limit = request_args.get('limit', 0)
            offset = request_args.get('offset', 0)

            request_args.pop('limit', None)
            request_args.pop('offset', None)

            cities = City.query.filter_by(**request_args)

            if limit:
                cities = cities.limit(limit)
            if offset:
                cities = cities.offset(offset)

            cities = cities.all()
            if not cities and (request_args or limit or offset):
                return abort(404, description = "No cities found matching the criteria")

            return marshal({
                'total': len(cities),
                'cities': marshal([city for city in cities], city_fields)
            }, city_list_fields)

    @marshal_with(city_fields)
    def post(self):  
        args = args_parser.parse_args()
        if args['id']:
            existing_city = City.query.get(args['id'])
            if existing_city:
                abort(409, description = "City with such id already exists")
        city = City(**args)

        db.session.add(city)
        db.session.commit()

        return city
    
    @marshal_with(city_fields)
    def put(self, city_id = None):
        city = City.query.get_or_404(city_id, description= 'City does not exist')

        if 'id' in request.get_json():
            city.id = request.json['id']
        if 'name' in request.get_json():
            city.name = request.json['name']

        db.session.commit()

        return city
    
    @marshal_with(city_fields)
    def delete(self, city_id = None):
        city = City.query.get_or_404(city_id, description= 'City does not exist')

        db.session.delete(city)
        db.session.commit()

        return city