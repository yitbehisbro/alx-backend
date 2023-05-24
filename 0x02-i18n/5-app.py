#!/usr/bin/env python3
'''Flask app'''
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config():
    '''Babel config'''
    LANGUAGES = ['en', 'fr']


app.config.from_object(Config)
Babel.default_locale = 'en'
Babel.default_timezone = 'UTC'

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale():
    '''Get locale from request'''
    locale = request.args.get("locale")
    if locale:
        return locale
    return request.accept_languages.best_match(Config.LANGUAGES)


def get_user():
    '''Return user from db'''
    login_as = request.args.get("login_as", False)
    if login_as:
        user = users.get(int(login_as), False)
        if user:
            return user
    return None


@app.before_request
def before_request():
    '''Before request'''
    user = get_user()
    g.user = user


@app.route('/', methods=['GET'])
def index():
    '''Return index'''
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
