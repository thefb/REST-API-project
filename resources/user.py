import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel


class UserRegistro(Resource):
    conexao = sqlite3.connect('data.db')
    cursor = conexao.cursor()
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="Este campo nao pode estar em branco"
        )
    parser.add_argument('password',
        type=str,
        required=True,
        help="Este campo nao pode estar em branco"
        )

    def post(self):
        data = UserRegistro.parser.parse_args()
        
        if UserModel.encontrar_por_id(data['username']):
            return {"mensagem": "Usuario ja existe."}, 400

        user = UserModel(data['username'], data['password'])
        user.save_to_db()

        return {"mensagem": "Usuario criado com sucesso."}, 201