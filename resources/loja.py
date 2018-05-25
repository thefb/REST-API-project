from flask_restful import Resource
from models.loja import LojaModel


class Lojas(Resource):
    def get(self, nome):
        loja = LojaModel.encontrar_por_nome(nome)
        if loja:
            return loja.json()
        return {'mensagem': 'Loja nao encontrada'}, 404

    def post(self, nome):
        if LojaModel.encontrar_por_nome(nome):
            return {'mensagem': "Uma loja com o nome '{}' ja existe.".format(nome)}, 400
        
        loja = LojaModel(nome)
        try:
            loja.save_to_db()
        except:
            return {'mensagem': "Ocorreu um erro inserindo o item."}, 500

        return loja.json(), 201

    def delete(self, nome):
        loja = LojaModel.encontrar_por_nome(nome)
        if loja:
            try:
                loja.delete_from_db()
            except:
                return {'mensagem': "Ocorreu um erro inserindo o item."}, 500
        
        return {'mensagem': "Loja deletada com sucesso!"}




class LojaLista(Resource):
    def get(self):
        return {'lojas': [lojas.json() for lojas in LojaModel.query.all()]}