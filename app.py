from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///memo.db'  # 後でRDSに切り替え
db = SQLAlchemy(app)

class Memo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    body = db.Column(db.Text)

@app.route('/')
def index():
    memos = Memo.query.all()
    return render_template('index.html', memos=memos)

@app.route('/add', methods=['POST'])
def add():
    memo = Memo(title=request.form['title'], body=request.form['body'])
    db.session.add(memo)
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)