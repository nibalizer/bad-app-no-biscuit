from server import app
from flask import render_template

def calc_fib(i):
    if i is 0:
        return 0
    
    total = 1
    prev_total = 0
    for i in range(i-1):
        temp = total + prev_total
        prev_total = total
        total = temp

    return(total)

@app.route('/')
def hello_world():
    return app.send_static_file('index.html')

@app.route('/fib/<val>')
def fib(val):
    var = calc_fib(int(val))
    return "The value is {}\n".format(str(var))

@app.errorhandler(404)
@app.route("/error404")
def page_not_found(error):
    return app.send_static_file('404.html')

@app.errorhandler(500)
@app.route("/error500")
def requests_error(error):
    return app.send_static_file('500.html')
