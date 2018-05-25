from db import db

class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(80))
    preco = db.Column(db.Float(precision=2))

    loja_id = db.Column(db.Integer, db.ForeignKey('lojas.id'))
    loja = db.relationship('LojaModel')

    def __init__(self, nome, preco, loja_id):
        self.nome = nome
        self.preco = preco
        self.loja_id = loja_id

    def json(self):
        return {'nome': self.nome, 'preco': self.preco}

    @classmethod
    def encontrar_por_nome(cls, nome):
        return cls.query.filter_by(nome=nome).first()
        
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
    