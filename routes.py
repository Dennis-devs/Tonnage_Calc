from flask import render_template, request, redirect, url_for
from models import Variables
from sqlalchemy import text

def register_routes(app, db):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/form', methods=['GET', 'POST'])
    def form():
        if request.method == 'GET':
            return render_template('form.html')
        elif request.method == 'POST':
            volume = request.form.get('volume')
            density = request.form.get('density')
            temperature = request.form.get('temperature')
            sql_statement = text("SELECT vcf FROM table60b WHERE volume=volume AND density=density")
            vcf = Variables.query.from_statement(sql_statement).params(volume=volume, density=density).first()

            Tonnage = (volume * density * vcf) / 1000 

            variables = Variables(
                volume=int(volume),
                density=float(density),
                Temperature=float(temperature),
                vcf=float(vcf),
                Tonnage=float(Tonnage)
            ) 
            
            db.session.add(variables)
            db.session.commit()


            return render_template('form.html', volume=volume, density=density, temperature=temperature, vcf=vcf)
        

