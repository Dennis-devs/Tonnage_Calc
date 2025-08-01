from app import db

class Variables(db.Model): 
       __tablename__='oil_tonnages'

       pid = db.Column(db.Integer, primary_key=True)
       volume = db.Column(db.Integer, nullable=False)
       density = db.Column(db.Numeric, nullable=False)
       Temperature = db.Column(db.Numeric, nullable=False)
       vcf = db.Column(db.Numeric)
       Tonnage = db.Column(db.Numeric)

       