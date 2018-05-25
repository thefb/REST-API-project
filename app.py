from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegistro
from resources.item import Item, ItemList
from resources.loja import Lojas, LojaLista


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'fabs'
api = Api(app)


jwt = JWT(app, authenticate, identity)

api.add_resource(Item, '/item/<string:nome>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegistro, '/register')
api.add_resource(LojaLista, '/lojas')
api.add_resource(Lojas, '/loja/<string:nome>')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True) # important to mention debug=True