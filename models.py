from app import db

class Variables(db.Model): 
       __tablename__='oil_tonnages'

       id = db.Column(db.Integer, primary_key=True, autoincrement=True)
       volume = db.Column(db.Numeric, nullable=False)
       density = db.Column(db.Numeric, nullable=False)
       temperature = db.Column(db.Numeric, nullable=False)
       vcf = db.Column(db.Numeric)
       Tonnage = db.Column(db.Numeric)

class Vcftable(db.Model): 
       __tablename__='table60b'

       id = db.Column(db.Integer, primary_key=True)
       density = db.Column(db.Numeric)
       temperature = db.Column(db.Numeric)
       vcf = db.Column(db.Numeric)
       class_ = db.Column('class', db.Numeric, nullable=True) 
       vcf2 = db.Column(db.Numeric, nullable=True)    