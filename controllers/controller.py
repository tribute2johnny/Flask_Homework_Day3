from app import app
from flask import render_template
from models.order_list import orders as all_orders

@app.route('/')
def index():
    return "Welcome to the store"

@app.route('/orders')
def orders():
    return render_template('index.html', title="All Orders", all_orders=all_orders)