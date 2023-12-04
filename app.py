from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Use o banco de dados SQLite como exemplo
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

# Crie as tabelas (execute este trecho uma vez para criar as tabelas)
with app.app_context():
    db.create_all()

# Adicione produtos ao banco de dados (execute este trecho uma vez para adicionar os produtos)
with app.app_context():
    products = [
        Product(name='Chocolate', price=5.99),
        Product(name='Baunilha', price=4.99),
        Product(name='Veludo Vermelho', price=7.99),
        Product(name='Dúzia', price=4.99)
    ]

    db.session.bulk_save_objects(products)
    db.session.commit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return render_template("sobre.html")

@app.route('/compras')
def comprar():
    # Recupere os produtos do banco de dados
    products = Product.query.all()
    return render_template("compras.html", products=products)

if __name__ == '__main__':
    app.run(debug=True)
