from flask import Flask, render_template

app = Flask(__name__)

@app.route('/ben')
def ben():
    return render_template('ben.html')

@app.route('/henry')
def henry():
    return render_template('henry.html')

@app.route('/b')
def b():
    return render_template('b.html', name = ["ben", "harry", "bob", "jay", "matt", "bill"] )

if __name__ == '__main__':
    app.run(debug = True)