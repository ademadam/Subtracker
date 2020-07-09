import sys
import subprocess
import requests



target = sys.argv[1]
host = sys.argv[2]


def brute():
  subprocess.check_call(["python", "sublist3r.py","-d",sys.argv[1],"-o","2.txt"])
  post()






cookies = {
}

headers = {
    '$Host': sys.argv[2],
    '$Upgrade-Insecure-Requests': '1',
    '$Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    '$Accept-Encoding': 'gzip, deflate',
    '$Content-Type': 'application/x-www-form-urlencoded',
    '$Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
}










a = open('1.txt', "r")
b = open('2.txt', "r")
c = []



 
def post():
  for domain in b :
    if domain not in a:
      c.append(domain)
      data = 'domain='+str(domain)
      response = requests.post('http://'+ sys.argv[2], headers=headers, cookies=cookies, data=data, verify=False)
      





















data = data2 = "" 
with open('1.txt') as fp: 
    data = fp.read() 
  

with open('2.txt') as fp: 
    data2 = fp.read() 
  

data += "\n"
data += data2 
  
with open ('1.txt', 'w') as fp: 
    fp.write(data) 
       
      


brute()
