from flask import render_template, request, redirect, url_for
from models import Variables, Vcftable
from sqlalchemy import text
import requests

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
                volume=volume,
                density=density,
                temperature=temperature,
                vcf=vcf,
                Tonnage=Tonnage
                ) 
                db.session.add(variables)
                db.session.commit()
                return render_template('form.html', vcf=vcf, Tonnage=Tonnage, summary= f"Using a Volume correction Factor of {vcf} given volume of {volume}, temperature of {temperature}, and density of {density}, the Tonnage(MT) is {Tonnage}")
            
            elif vcf_value is None:
                return render_template('form.html', error="No VCF found for the given Temperature and Density.")
               
        return render_template('form.html')

    @app.errorhandler(500)
    def internal_error(error):
        return render_template('500.html'), 500
    
    # Sorting and Searching
    @app.route('/search')
    def search():
        search_by = request.args.get('search-by')
        search_value = request.args.get('search-value')
        sort_by = request.args.get('sort-by')
       
        search_statement = text(f"SELECT * FROM oil_tonnages WHERE {search_by} = :search_value ORDER BY {sort_by}")
        
        # Validate search_by and sort_by against known columns to prevent SQL injection
        table_colmns = ['volume', 'density', 'temperature', 'vcf', 'Tonnage']

        if search_by not in table_colmns or sort_by not in table_colmns:
            return render_template('form.html', search_error="Invalid search criteria. Please select a valid column to search by.")
        else:
            search_values = db.session.query(Variables).from_statement(search_statement).params(search_value=search_value, sort_by=sort_by, search_by=search_by).all()
        

        # Render the search results
        if search_values:
            return render_template('form.html', search_values=search_values)
        else:
            return render_template('form.html', search_error="No results found for the given search criteria.")
          
            
            


            
        

