from flask import Flask, render_template, request, redirect, url_for, flash, make_response
app = Flask('__main__')

@app.route('/<var>')
def index(var):
	resp = make_response("hello")
	resp.set_cookie("userr", "123456")
	return(resp)



@app.route('/getcookie')
def getcookie():
   name = request.cookies.get('userr')
   return '<h1>welcome '+str(name)+'</h1>'

@app.route('/')
def bs():
	return render_template('bootstrap.html')



app.run(debug = True, port = 8000)