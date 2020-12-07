from flask import Flask, render_template, g, request, redirect, url_for
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db_uri = os.environ.get('DATABASE_URL') or "postgresql://localhost/flasknote"

app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
db = SQLAlchemy(app)

class Entry(db.Model):
    __tablename__ = "companies"
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(), nullable=False)
    type = db.Column(db.String(), nullable=False)
    phone = db.Column(db.String(), nullable=False)
    address = db.Column(db.String(), nullable=False)

@app.route('/')
def companylist():
    companies = Entry.query.all() #変更
    return render_template('index.html', companies=companies)

@app.route('/post', methods=['POST'])
def add_company():
    company = Entry()
    company.company_name = request.form['name']
    company.type = request.form['type']
    company.phone = request.form['phone']
    company.address = request.form['address']
    db.session.add(company)
    db.session.commit()
    return redirect(url_for('companylist'))
