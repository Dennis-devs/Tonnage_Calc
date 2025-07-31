from app import db

class User(db.Model): 
       __tablename__='Measurements'

       pid = db.Column(db.Integer, primary_key=True)
       volume = db.Column(db.Integer, nullable=False)
       density = db.Column(db.Integer, nullable=False)
       Temperature = db.Column(db.Integer, nullable=False)
       vcf = db.Column(db.Integer)

       def __repr__(self):
            return f'<User: {self.username}, Role: {self.role}>'
       def get_id(self):
            return self.uid