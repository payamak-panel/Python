from lib.rest import Rest_Client
# Use bellow lines to consume with a `pip install payamak-panel`
# from payamak-panel import rest
# Rest_Client = rest.Rest_Client

restClient = Rest_Client('username', 'password')
result = restClient.SendSMS('09123456789', '5000xxx', 'test sms')

# restClient.GetDeliveries2(12345678)
# restClient.GetMessages(1234, '5000xxx', 0, 100)
# restClient.BaseServiceNumber('test sms', '09123456789', 123456)
# restClient.GetUserNumbers()
# restClient.GetBasePrice()
# restClient.GetCredit()

print(result)
# print(result['Value']) #access values inside json response
