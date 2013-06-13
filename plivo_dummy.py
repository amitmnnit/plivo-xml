import plivo


auth_id = "MAZWVMNMY4ZWUYYTEXYZ"
auth_token = "OGMyOThlZDkzMzZlN2FiMzg2NzY4ZmI4ZmFiMzQ4"

p = plivo.RestAPI(auth_id, auth_token)

# Get account
params = {
	'country_iso' : 'US',
	'number_type' : 'tollfree',
	'country_code' : '1'
}
response = p.search_numbers(params)

print response[0]
res = response[1]
for key in res.keys():
	print key,' : ',res[key], '\n'