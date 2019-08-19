import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError
'''
Convert db to json
'''
class DecimalEncoder(json.JSONEncoder):
	def default(self, o):
		if isinstance(o, decimal.Decimal):
			if o % 1 > 0:
				return float(o)
			else:
				return int(o)
		return super(DecimalEncoder, self).default(o)

table = boto3.resource('dynamodb', region_name = 'us-west-2').Table('stock_table')

response = table.scan(
	FilterExpression = Key('Stock Price').between(0,1000),
	ProjectionExpression = "#t, #st",
	ExpressionAttributeNames = {"#t":"Ticker", "#st" : "Stock Price"}
	)
#print(response)
s_list = []
for i in response['Items']:
	print(json.dumps(i,cls = DecimalEncoder))
	#with open("stock_list.json", "w") as foo:
		#foo.write(json.dumps(i,cls=DecimalEncoder))
	s_list.append(json.dumps(i,cls=DecimalEncoder))
	#with open("stock_list.json") as bar:
	#	s_dict = json.load(bar,)
	#print("SDICT =", s_list)
while 'LastEvaluatedKey' in response:
	response = table.scan(
		FilterExpression = Key('Ticker').between(100,300),
		ProjectionExpression = "#t, #st",
		ExpressionAttributeNames = {"#t" : "Ticker", "#st" : "Stock Price"},
		ExclusiveStartKey=response['LastEvaluatedKey']
	)
	for i in response['Items']:
		print(json.dumps(i,cls=DecimalEncoder))
		s_list.append(json.dumps(i,cls=DecimalEncoder))
		#with open("stock_list.json", "w") as foo:
		#	foo.write(json.dumps(i,cls=DecimalEncoder))
print(s_list)

