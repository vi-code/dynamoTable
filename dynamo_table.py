import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('stock_table')

table.put_item(
	Item={
		'Ticker': 'SPY',
		'Cost': 288,
		'Sentiment': 'Bearish'

	}
)
