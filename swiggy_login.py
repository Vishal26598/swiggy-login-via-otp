import re
import requests, lxml.html
s = requests.session()

login = s.get('https://www.swiggy.com/dapi/cart')
print(login.text)
cart_csrf = re.findall("en\":\"(.*)\"}",login.text)
mobile = input("enter mobile no: ")
form = {'mobile': mobile}
form['_csrf'] = cart_csrf[0]
print(form)
print()
print()
head = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
login = s.post('https://www.swiggy.com/dapi/auth/sms-otp', data = form)
print(login.headers)
print(login.request.headers)
print(login.cookies)
print(login.status_code)
print(login.text)
print()
print()
login = s.post('https://www.swiggy.com/dapi/auth/sms-otp', data = form)
# login = s.post('https://www.swiggy.com/dapi/auth/sms-otp', data = form)
print(login.headers)
print(login.request.headers)
print(login.cookies)
print(login.status_code)
print(login.text)
cart_csrf = re.findall("en\":\"(.*)\"}",login.text)
otp = input("enter otp: ")
form1 = {'otp': otp}
form1['_csrf'] = cart_csrf[0]
login = s.post('https://www.swiggy.com/dapi/auth/otp-verify', data = form1, headers = head)
login = s.get('https://www.swiggy.com/bangalore/restaurants')
# print(login.text)
