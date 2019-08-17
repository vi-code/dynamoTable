import boto3
import json
import decimal

table = boto3.resource('dynamodb', region_name = 'us-west-2').Table('stock_table')

'''	table.put_item(
	Item = {
		'Ticker' : 'DIA',
		'Stock Price' : 255
	}
)
'''
#print('here')
with open("stocks.json") as json_file:
	stocks = json.load(json_file, parse_float = decimal.Decimal)
	for stock in stocks:
		ticker = stock['Ticker']
		price = int(stock['Stock Price'])

		print("New Stock Added: ", ticker, price)
		table.put_item(
			Item = {
				'Ticker' : ticker,
				'Stock Price' : price,
			}
		)
