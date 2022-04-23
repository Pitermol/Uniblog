from controllers.BaseController import *
from models import *


class PageController(BaseController):
    def _call(self, *args, **kwargs):
        page = kwargs.get('page', False)

        if page == 'index':
            return self.index_page()
        elif page == '404error' or page == '405error':
            return self.error_page(kwargs['error'])
        elif page == 'registration':
            return self.registration()
        elif page == 'auth':
            return self.auth()


    def index_page(self):
        # производим проверку, авторизирован ли пользователь
        # в зависимости от ответа кидаем ему статику
        login = session.get('login', False)
        password = session.get('password', False)
        is_auth = login and password

        return render_template('index.html', is_auth=is_auth, login=login)

    
    def registration(self):
        # регистрируем юзера, добавляем в БД строку
        login, possword = self.request.values['login'], self.request.values['password']
        return redirect(url_for('index'))


    def auth(self):
        # подтягиаем данные из БД, добавляем их в сессию
        login  = self.request.values['login']
        password = self.request.values['password']

        session['login'] = login
        session['password'] = password

        return redirect(url_for('index'))


    def error_page(self, error_code):
        if error_code == 404:
            return render_template('404.html'), 404
        elif error_code == 405:
            return redirect(url_for('index'))
