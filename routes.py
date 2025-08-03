from flask import render_template, request, redirect, url_for
from models import Variables, Vcftable
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
            sql_statement = text("SELECT id, vcf FROM table60b WHERE temperature = :temperature AND density = :density")
            vcf_value = db.session.query(Vcftable).from_statement(sql_statement).params(temperature=temperature, density=density).first()

            # Calculate Tonnage if vcf_value is found
            if vcf_value:
                vcf = float(vcf_value.vcf)
                volume = float(volume)
                density =float(density)
                Tonnage = (volume * density * vcf) / 1000

                variables = Variables(
                id=1,
                volume=volume,
                density=density,
                temperature=temperature,
                vcf=vcf,
                Tonnage=Tonnage
                ) 
                
                db.session.add(variables)
                db.session.commit()

                return render_template('form.html', vcf=vcf, Tonnage=Tonnage)

            elif vcf_value is None:
                return render_template('form.html', error="No VCF found for the given volume and density.")
        return render_template('form.html')


            
            
            


            
        

