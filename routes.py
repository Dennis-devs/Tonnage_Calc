from flask import render_template, request, redirect, url_for


def register_routes(app, db):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/form', methods=['GET', 'POST'])
    def form():
        if request.method == 'GET':
            return render_template('form.html')
        elif request.method == 'POST':
            task = request.form.get('task')
            Tasks = []
            if task:
                Tasks.append(task)
            # Tasks = Tasks.append(task)
            return render_template('index.html', Tasks=Tasks)

