from db import db

class LojaModel(db.Model):
    __tablename__ = 'lojas'

    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(80))

    items = db.relationship('ItemModel', lazy='dynamic')

    def __init__(self, nome):
        self.nome = nome

    def json(self):
        return {'nome': self.nome, 'items': [x.json() for x in self.items.all()]}

    @classmethod
    def encontrar_por_nome(cls, nome):
        return cls.query.filter_by(nome=nome).first()
        
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
    