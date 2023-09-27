from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/hello')
def hello():
    return '<html><body><h1>Hello World</h1></body></html>'
    #return render_template('hello.html')

@app.route('/hello/<user>')
def hello_name(user):
    return render_template('hello.html', name=user)

@app.route('/score/<int:score>')
def display_score(score):
    return render_template('score.html', marks=score)

@app.route('/result')
def result():
    result_dict = {'phy': 50, 'che': 60, 'maths': 70}
    return render_template('result.html', result=result_dict)

@app.route('/table/<int:num>')
def table(num):
    return render_template('print-table.html', n=num)

if __name__ == '__main__':
    app.run(debug=True)
