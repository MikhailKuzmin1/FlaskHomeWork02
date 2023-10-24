from flask import Flask, make_response, redirect, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login = request.form.get('login')
        mail = request.form.get('mail')
        responce = make_response(redirect('/hello'))
        responce.set_cookie('name', login)
        responce.set_cookie('Email', mail)
        return responce
    return render_template('base.html')

@app.route('/hello')
def hello():
    name = request.cookies.get('name')
    if name:
        return render_template('hello.html', name=name )
    return redirect('/')

@app.route('/quit')
def quit():
    response = make_response(redirect('/'))
    response.delete_cookie('name')
    response.delete_cookie('Email')
    return response


if __name__ == '__main__':
    app.run(debug=True)
