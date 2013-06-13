import plivo


r = plivo.Response()


# Add speak
body = 'Calling from Plivo'
params = {'loop':2}

r.addSpeak(body, **params)