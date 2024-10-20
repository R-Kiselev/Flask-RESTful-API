from flask import url_for, request

DEFAULT_PAGE = 1
DEFAULT_PAGE_SIZE = 5

def extract_pagination(page=None, per_page=None, **kwargs):
    page = int(page) if page is not None else DEFAULT_PAGE
    per_page = int(per_page) if per_page is not None else DEFAULT_PAGE_SIZE
    return page, per_page

def apply_filters(query):
    filter_params = {}
    for key, value in request.args.items():
        if key not in ['page', 'per_page']:
            filter_params[key] = value
    
    return query.filter_by(**filter_params), filter_params

def paginate(query, schema):
    page, per_page = extract_pagination(page=request.args.get('page'), per_page=request.args.get('per_page'))
    
    query, filter_params = apply_filters(query)
    
    page_obj = query.paginate(page=page, per_page=per_page)
    
    next_ = url_for(
        request.endpoint,
        page=page_obj.next_num if page_obj.has_next else page_obj.page,
        per_page=per_page,
        **request.view_args,
        **filter_params
    )
    prev_ = url_for(
        request.endpoint,
        page=page_obj.prev_num if page_obj.has_prev else page_obj.page,
        per_page=per_page,
        **request.view_args,
        **filter_params
    )

    return {
        'total': page_obj.total,
        'pages': page_obj.pages,
        'next': next_,
        'prev': prev_,
        'results': schema.dump(page_obj.items, many=True)
    }, 200
