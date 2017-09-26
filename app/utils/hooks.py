# -*- coding: utf-8 -*-

import falcon
from app.errors import UnauthorizedError


def auth_required(req, res, resource, *args, **kwargs):
    if req.context['auth_user'] is None:
        raise UnauthorizedError()
