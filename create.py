import boto3


dynamodb = boto3.client('dynamodb', region_name = 'us-west-2')

try:
	table = dynamodb.create_table(
		TableName = 'stock_table',
		KeySchema =[
			{
				'AttributeName': 'Ticker',
				'KeyType' : 'HASH'
			},
			{
				'AttributeName': 'Stock Price',
				'KeyType': 'RANGE'
			}
		],
		AttributeDefinitions=[
			{
				'AttributeName': 'Ticker',
				'AttributeType': 'S',
			},
			{
				'AttributeName': 'Stock Price',
				'AttributeType': 'N'
			},
		],
		ProvisionedThroughput={
	    	'ReadCapacityUnits': 10,
	    	'WriteCapacityUnits': 10
	    }
	)
except dynamodb.exceptions.ResourceInUseException:
	pass
#	table = dynamodb.Table('stock_table')
print("Status: ", boto3.resource('dynamodb', region_name = 'us-west-2').Table('stock_table').table_status)
