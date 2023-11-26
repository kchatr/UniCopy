from flask import Blueprint, jsonify, request
import random
import string
import requests
from sqlalchemy import desc
import json
import urllib.request
from datetime import datetime, timedelta
import apscheduler
from apscheduler.schedulers.background import BackgroundScheduler
from pytz import timezone

import cohere
from documents import Documents
from chatbot import Chatbot
from preprocessing import get_sources

co = cohere.Client("Gx29SVN2CnTY3yZtqJQEYwgfQpSlN6m11yMU1mpF")

sources = get_sources()

documents = Documents(sources, co)

chatbot = Chatbot(documents, co)

# api_key = 'OTKHLLKZ9SXFZUHP'
api_key = 'DNWQMLFC43J1PHDI'


main = Blueprint('main', __name__)




@main.route('/get_response', methods=['POST'])



def get_response():
    # Assuming you want to process the input text in some way
    input_text = request.json['text']

    prompt = f"""
        Below is a patent idea. Please provide any patents that are the most similar or contain similar topics.

        {input_text}

        For any patents used, please provide the corresponding patent number.
    """

    chatbot_response = chatbot.generate_response(prompt)
    processed_text = chatbot_response.text  # Example processing, you can customize this
    return jsonify({'result': processed_text})

# def get_responses():
#     input_text = request.json['text']
#     return jsonify({'result':input_text})

  
    

# @main.route('/add_data', methods=['POST'])



# def add_data():

#     request_data = request.json
#     name_data = request_data['query'].upper()
#     amount_data = int(request_data['amount'])

#     portfolio = Portfolio_Log.query.order_by(desc(Portfolio_Log.time)).first()

#     url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={name_data}&apikey={api_key}'
#     response = requests.get(url)
#     data = response.json()

#     if data['Global Quote'] and amount_data is not None and portfolio:

#         stock_data = data['Global Quote']

#         current_price = float(stock_data['05. price']) + 0.00

#         previous_close = float(stock_data['08. previous close'])

#         change = current_price - previous_close

#         percent_change = (change / previous_close) * 100

#         price_bought_at = current_price

#         average_price = current_price

#         value = average_price * amount_data

#         new_stock = Stock(name = name_data, price = current_price, prev_price=previous_close, change=change, percent_change=percent_change, amount=amount_data, price_bought_at=price_bought_at, average_price=average_price, value=value, date_updated = datetime.now(timezone('EST')).date())
        
#         #adding to portfolio db
#         new_value = portfolio.value + value

#         new_portfolio_log = Portfolio_Log(value=new_value, initial_value=new_value, change=portfolio.change, percent_change=portfolio.percent_change)

#         article_data = news_search(name_data)[0]

#         new_article = News_Item(time=article_data['publishedAt'], stock_name=name_data, article_name= article_data['title'], article_description= article_data['description'], url= article_data['url'], image= article_data['image'], publisher_url= article_data['source']['url'], publisher_name= article_data['source']['name'])

#         db.session.add(new_stock)
#         db.session.add(new_article)
#         db.session.add(new_portfolio_log)
#         db.session.commit()

#         return jsonify({'ok'})

#     else:
#         return jsonify({'not ok'})
    




# @main.route('/get_data', methods = ['GET'])

# def get_data():

#     stock_list = Stock.query.order_by(Stock.id).all()

#     stocks = []

#     for stock in stock_list:
#         stocks.append({'name': stock.name, 'price': stock.price, 'prev_price': stock.prev_price, 'change':stock.change, 'percent_change': stock.percent_change, 'amount': stock.amount, 'price_bought_at': stock.price_bought_at, 'average_price': stock.average_price, 'value':stock.value})

#     return jsonify({'stocks':stocks})

# @main.route('/get_portfolio', methods = ['GET'])


# def get_portfolio():

#     portfolio = Portfolio_Log.query.order_by(desc(Portfolio_Log.time)).first()


#     return jsonify({'portfolio':{'time': portfolio.time, 'change': portfolio.change, 'percent_change': portfolio.percent_change, 'initial_value': portfolio.initial_value, 'value': portfolio.value}})


# @main.route('/check_stock', methods = ['POST'])

# def check_stock():

#     stock_add = request.json['query'].upper()

#     url = f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={stock_add}&apikey={api_key}'

#     r = requests.get(url)
#     data = r.json()

#     if 'bestMatches' in data and len(data['bestMatches']) > 0:
#         return jsonify({'validity': True})
#     else:
#         return jsonify({'validity': False})



# @main.route('/already_added', methods = ['POST'])

# def already_added():

#     stock_name = request.json['query'].upper()

#     stock_list = Stock.query.all()

#     for stock in stock_list:

#         if stock.name == stock_name:
#             return jsonify({'added': True})
    
    
#     return jsonify({'added': False})



# @main.route('/increase_amount', methods = ['PUT'])

# def increase_amount():
#     try:
#         stock_name = request.json['selected_stock'].upper()
#         # stock_name = 'AAPL'

#         # url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={stock_name}&apikey={api_key}'

#         # response = requests.get(url)
#         # data = response.json()

#         # stock_data = data['Global Quote']

#         # current_price = float(stock_data['05. price']) + 0.00


#         row = Stock.query.filter_by(name=stock_name).order_by(Stock.id).first()

#         # portfolio = Stock.query.order_by(desc(Stock.id)).first()

#         portfolio = Portfolio_Log.query.order_by(desc(Portfolio_Log.time)).first()


#         if row is None:
#             return 'row does not exist, error', 404


#         # row.average_price = (row.average_price*row.amount + current_price)/(row.amount + 1)

#         row.amount += 1

#         new_value = portfolio.value + row.average_price

#         new_portfolio_log = Portfolio_Log(value=new_value, initial_value=new_value, change=portfolio.change, percent_change=portfolio.percent_change)

#         db.session.add(new_portfolio_log)

#         db.session.commit()

#         return "row updated successfully"
    
#     except Exception as e:
#         print(e, 'ahhhh help an error')

#         return 'oopsy'


# @main.route('/decrease_amount', methods=['PUT'])

# def decrease_amount():
#     try:
#         stock_name = request.json['selected_stock'].upper()

#         # url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={stock_name}&apikey={api_key}'

#         # response = requests.get(url)
#         # data = response.json()

#         # stock_data = data['Global Quote']

#         # current_price = float(stock_data['05. price']) + 0.00

#         row = Stock.query.filter_by(name=stock_name).order_by(Stock.id).first()

#         # portfolio = Portfolio_Log.query.order_by(desc(Portfolio_Log.id)).first()

#         portfolio = Portfolio_Log.query.order_by(desc(Portfolio_Log.time)).first()


#         if row is None:
#             return 'row does not exist, error', 404

#         if row.amount != 0:
#             row.amount -= 1

#             new_value = portfolio.value - row.average_price

#             new_portfolio_log = Portfolio_Log(value=new_value, initial_value=new_value, change=portfolio.change, percent_change=portfolio.percent_change)

#             db.session.add(new_portfolio_log)


#         db.session.commit()

#         return "row updated successfully"
    
#     except Exception as e:
#         print(e)

#     return "error occurred"  # Add a return statement here

# @main.route('/delete_stock', methods=['DELETE'])

# def delete_stock():

#     stock_name = request.json['selected_stock'].upper()

#     row = Stock.query.filter_by(name=stock_name).order_by(Stock.id).first()

#     # portfolio = Portfolio_Log.query.order_by(desc(Portfolio_Log.id)).first()

#     portfolio = Portfolio_Log.query.order_by(desc(Portfolio_Log.time)).first()

#     article = News_Item.query.filter_by(stock_name=stock_name).first()


#     if row:

#         new_value = portfolio.value - (row.average_price * row.amount)

#         new_portfolio_log = Portfolio_Log(value=new_value, initial_value=new_value, change=portfolio.change, percent_change=portfolio.percent_change)

#         db.session.add(new_portfolio_log)

#         db.session.delete(row)

#         db.session.delete(article)

#         db.session.commit()
#         return jsonify({'message': 'Stock deleted successfully'})
#     else:
#         return jsonify({'error': 'Stock not found'})

   
# @main.route('/graph_portfolio', methods=['GET'])

# def graph_portfolio():

#     data = Portfolio_Log.query.all()
#     graph_data = [ {'time': row.time.strftime('%Y-%m-%d %H:%M:%S.'), 'value': row.value} for row in data ]

#     return jsonify(graph_data)


# @main.route('/add_article', methods=['POST'])
# def add_article():
    
#     # try:
#     stock_name = request.json['selected_stock'].upper()
#         # stock_name = 'AAPL'

#         # # Use query attribute of News_Item model to create the query
#     news_item = News_Item.query.filter_by(stock_name=stock_name).first()

    
#     # news_item = True
#     if not news_item:
#         article_data = news_search(stock_name)[0]

#         new_article = News_Item(stock_name=stock_name, article_name= article_data['title'], article_description= article_data['description'], url= article_data['url'], image= article_data['image'], publisher_url= article_data['source']['url'], publisher_name= article_data['source']['name'])

#         db.session.add(new_article)
#         db.session.commit()

#         news_item = News_Item.query.filter_by(stock_name=stock_name).first()
#         return 'added'
    
#     return 'element already added'
#         # return jsonify({'news_article': {'stock_name': news_item.stock_name, 'article_name': news_item.article_name, "article_description": news_item.article_description, "url": news_item.url, "image": news_item.image, "publisher_url": news_item.publisher_url, 'publisher_name': news_item.publisher_name}})

# @main.route('/get_article', methods=['GET'])
# def get_article():

#     # stock_name = request.json['selected_stock'].upper()

#     stock_name = request.args.get('selected_stock', '').upper()


#     news_item = News_Item.query.filter_by(stock_name=stock_name).first()

#     return jsonify({'news_article': {'time': news_item.time, 'stock_name': news_item.stock_name, 'article_name': news_item.article_name, "article_description": news_item.article_description, "url": news_item.url, "image": news_item.image, "publisher_url": news_item.publisher_url, 'publisher_name': news_item.publisher_name}})



# @main.route('/get_stock_prices', methods=['GET'])
# def get_stock_prices():
#     stock_symbol = request.args.get('stock_name')
#     # stock_symbol = 'AAPL'
    
#     one_week_ago = datetime.now() - timedelta(days=14)

#     stock_data = StockData.query.filter_by(stock_name=stock_symbol).filter(StockData.date >= one_week_ago).order_by(StockData.date.asc()).all()

#     if not stock_data:

#         url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock_symbol}&apikey={api_key}"        
#         response = requests.get(url)

#         if response.status_code == 200:
           
#             stock_data = response.json()
#             # return jsonify(stock_data)

#             for date, price in stock_data['Time Series (Daily)'].items():
#                 new_data = StockData(stock_name=stock_symbol, date=date, price=float(price['4. close']))
#                 db.session.add(new_data)
#             db.session.commit()

#             stock_data = StockData.query.filter_by(stock_name=stock_symbol).filter(StockData.date >= one_week_ago).order_by(StockData.date.asc()).all()

#     result = [{'date': data.date, 'price': data.price} for data in stock_data]

#     return jsonify(result)

# @main.route('/daily_update', methods=['POST', 'PUT'])
# def daily_update():
#     list_of_stocks = [stock.name for stock in Stock.query.all()]

#     for stock in list_of_stocks:
#         # stocks.append(stock.name)
#         row = Stock.query.filter_by(name=stock).order_by(Stock.id).first()
#         old_portfolio = Portfolio_Log.query.order_by(desc(Portfolio_Log.time)).first()

#         if (row.date_updated == None) or (row.date_updated != datetime.now(timezone('EST')).date()):
#             url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={stock}&apikey={api_key}'
            
#             response = requests.get(url)
#             data = response.json()
#             stock_data = data['Global Quote']

#             row.date_updated = datetime.now(timezone('EST')).date()
#             row.time = datetime.now(timezone('EST'))
#             row.price = float(stock_data['05. price']) + 0.00
#             previous_close = float(stock_data['08. previous close'])
#             row.change = float(stock_data['05. price']) + 0.00 - previous_close
#             row.percent_change = ((float(stock_data['05. price']) + 0.00 - previous_close) / previous_close) * 100
#             row.average_price = float(stock_data['05. price']) + 0.00
#             row.value = (float(stock_data['05. price']) + 0.00) * row.amount

#             portfolio_change = float(stock_data['05. price']) + 0.00 - old_portfolio.initial_value
#             portfolio_percent_change = portfolio_change/old_portfolio.initial_value
            
#             new_portfolio_log = Portfolio_Log(value=float(stock_data['05. price']) + 0.00, initial_value=old_portfolio.initial_value, change=portfolio_change, percent_change=portfolio_percent_change)

#             db.session.add(new_portfolio_log)

#     db.session.commit()


#     return 'ok'
