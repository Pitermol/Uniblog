from flask import request, render_template, make_response, url_for, redirect, session
import re
from models import *


def is_auth():
    login = session.get('login', False)
    password = session.get('password', False)
    if not login or not password:
        return False
    u = User.select().where(User.login==login).first()
    return u.password == password


class BaseController:
    def __init__(self):
        self.request = request

    def call(self, *args, **kwargs):
        print('in call')
        try:
            return self._call(*args, **kwargs)
        except Exception as ex:
            return make_response(str(ex), 500)

    def __call(self, *args, **kwargs):
        raise NotImplementedError('_call')



