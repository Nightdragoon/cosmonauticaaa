import requests
import socket

ip = input("pon mi ip:")
a = requests.get(url="http://localhost:8090/init" , params={"ip":"http://" + str(ip)})
print(a.text)