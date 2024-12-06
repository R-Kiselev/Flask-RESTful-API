import os
import dotenv
import click

from flask.cli import with_appcontext


dotenv.load_dotenv()


@click.command('init')
@with_appcontext
def init():
    """Create a new admin user"""
    from app.extensions import db
    from app.models.user import User
    from app.api.schemas.user import UserSchema

    admin_info = {
        'email': os.getenv('ADMIN_EMAIL'),
        'password': os.getenv('ADMIN_PASS'),
        'roles': ['admin'],
    }

    data = UserSchema().load(admin_info)
    if (User.query.filter_by(email=data.get('email', None)).first()):
        click.echo('Admin already exists')
        return

    admin = User(**data)

    db.session.add(admin)
    db.session.commit()
