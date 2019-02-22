from flask import Flask, render_template, redirect, url_for, flash, make_response, request
app = Flask(__name__)

num = 5             #total teams
arr = []
html_str = ""

for i in range(0,num):
	arr.append(0)


@app.route('/')
def index():
   #resp = make_response(render_template('innov.html'))
   #return (resp)
   return (render_template(('innov.html')))


@app.route('/setcookie')
def  check():
	resp = make_response(render_template('result.html'))
	resp.set_cookie("rakesh5", "123456")
	return (resp)

@app.route('/<var>')
def upvote(var):
	if(str(request.cookies.get('rakesh5')) == "None"):
		arr[int(var)] += 1
		return redirect('setcookie')
	else:
		return redirect('result')
	
 
@app.route('/result')
def result():
	html_str = " "
	for i in range(0, len(arr)):
		html_str += ("<label> team"+str(i)+"  ="+str(arr[i])+"</label><br>") 
	return(html_str)

if __name__ == '__main__':
   app.run(host= '0.0.0.0', port = '8080', debug = True)

