import time
import requests

start = time.time()
x = requests.post('http://127.0.0.1:5000/predict',
                  files={'image_bytes': open('assets/orange.jpg', 'rb').read()})
end = time.time()

print('Request-response time:', (end-start)*1000, 'ms')
print('Status code:', x.status_code)
print('Result:', x.text)

start = time.time()
x = requests.post('http://127.0.0.1:5000/predict',
                  files={'image_bytes': open('assets/icecream.jpg', 'rb').read()})
end = time.time()

print('Request-response time:', (end-start)*1000, 'ms')
print('Status code:', x.status_code)
print('Result:', x.text)