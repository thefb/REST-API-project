from flask_jwt import JWT, jwt_required, current_identity
from flask_restful import Resource, reqparse
import sqlite3
from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('preco',
        type=float,
        required=True,
        help="Este campo nao pode estar vazio!"
        )

    parser.add_argument('loja_id',
        type=int,
        required=True,
        help="Este campo nao pode estar vazio!"
        )

    @jwt_required()
    def get(self, nome):
        item = ItemModel.encontrar_por_nome(nome)
        if item:
            return item.json()
        return {'message': 'Item nao encontrado'}, 404


    def post(self, nome):
        if ItemModel.encontrar_por_nome(nome):
            return {'mensagem': "Um item com o nome '{}' ja existe.".format(nome)}, 400
        
        data = Item.parser.parse_args()

        item = ItemModel(nome, **data)
        
        try:
            item.save_to_db()
        except:
            return {'mensagem': "Ocorreu um erro inserindo o item."}, 500 #internal server error

        return item.json(), 201

    def delete(self, nome):
        item = ItemModel.encontrar_por_nome(nome)
        if item:
            item.delete_from_db()
        
        return {'mensagem': 'Item deletado'}

    def put(self, nome):
        data = Item.parser.parse_args()
        item = ItemModel.encontrar_por_nome(nome)
        
        if item:            
            item.preco = data['preco']
        else:
            item = ItemModel(nome, **data)
        
        item.save_to_db()

        return item.json()
    
class ItemList(Resource):
    def get(self):
        return {'items': [item.json() for item in ItemModel.query.all()]}

