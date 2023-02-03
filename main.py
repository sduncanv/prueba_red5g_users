from flask import Flask, request
from config.database import Database
from forms.forms import Singup, Login
from werkzeug.datastructures import ImmutableMultiDict
from services.services import Services

app = Flask(__name__)

@app.route('/singup', methods=['POST'])
def singup():
    try:
        form = Singup(ImmutableMultiDict(request.json))

        if request.method == 'POST' and form.validate():
            db = Database()
            res = Services(db).singup_user(request.json)
            return res
        else:
            return form.errors

    except Exception as e:
        return {'Error': str(e)}


@app.route('/login', methods=['POST'])
def login():
    try:
        form = Login(ImmutableMultiDict(request.json))

        if request.method == 'POST' and form.validate():
            db = Database()
            res = Services(db).login_user(request.json)
            return res
        else:
            return form.errors

    except Exception as e:
        return {'Error': str(e)}


if __name__ == '__main__':
    app.run(
        debug = True
    )