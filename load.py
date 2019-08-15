import boto3

table = boto3.resource('dynamodb', region_name = 'us-west-2').Table('stock_table')

table.put_item(
	Item = {
		'Ticker' : 'DIA',
		'Stock Price' : 255
	}
)
