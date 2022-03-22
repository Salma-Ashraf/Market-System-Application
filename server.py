from flask import Flask,request,jsonify
import product_DAO
from SQL_connection import get_sql_connection

app = Flask(__name__)
connection = get_sql_connection()
@app.route('/getproducts')

def get_all_products():
    products = product_DAO.get_all_products(connection)
    response = jsonify(products)
    response.headers.add('Acess-Allow-Control-Origin','*')
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server")
    app.run(port=5000)

