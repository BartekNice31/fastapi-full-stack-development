import time
import requests

url="https://httpbin.org/get"

def main():
    url="https://httpbin.org/get"
    session=requests.session()
    counter=10
    for i in range(counter):
        response=session.get(url)
        if response.status_code==200:
            print("Response received")
        
time_start=time.time()
main()
time_stop=time.time()
print(f"Elapsed time: {time_stop-time_start}")