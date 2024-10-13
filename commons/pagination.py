from flask import url_for, request

DEFAULT_PAGE = 1
DEFAULT_PAGE_SIZE = 5

def extract_pagination(page = None, per_page = None, **other_args):
    page = int(page) if page is not None else DEFAULT_PAGE
    per_page = int(per_page) if per_page is not None else DEFAULT_PAGE_SIZE
    return page, per_page, other_args

def paginate(query, schema):
    page, per_page, other_args = extract_pagination(**request.args)
    page_obj = query.paginate(page = page, per_page = per_page, **other_args)
    next_ = url_for(
        request.endpoint,
        page = page_obj.next_num if page_obj.has_next else page_obj.page,
        per_page = per_page,
        **other_args,
        **request.view_args
    )
    prev_ = url_for(
        request.endpoint,
        page = page_obj.prev_num if page_obj.has_prev else page_obj.page,
        per_page = per_page,
        **other_args,
        **request.view_args
    )
    return {
        'total' : page_obj.total,
        'pages' : page_obj.pages,
        'next' : next_,
        'prev' : prev_,
        'results' : schema.dump(page_obj.items, many= True)
    }, 200
