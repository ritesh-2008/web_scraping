#importing libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd

url="https://www.flipkart.com/laptop-accessories/keyboards/pr?sid=6bo%2Cai3%2C3oe&sort=popularity&p%5B%5D=facets.serviceability%5B%5D%3Dtrue&p%5B%5D=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&hpid=4Q-KuJnt9fiSTVnb1M6wAqp7_Hsxr70nj65vMAAFKlc%3D&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InZhbHVlQ2FsbG91dCI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ2YWx1ZUNhbGxvdXQiLCJpbmZlcmVuY2VUeXBlIjoiVkFMVUVfQ0FMTE9VVCIsInZhbHVlcyI6WyJXaXJlZCBhbmQgV2lyZWxlc3MiXSwidmFsdWVUeXBlIjoiTVVMVElfVkFMVUVEIn19LCJoZXJvUGlkIjp7InNpbmdsZVZhbHVlQXR0cmlidXRlIjp7ImtleSI6Imhlcm9QaWQiLCJpbmZlcmVuY2VUeXBlIjoiUElEIiwidmFsdWUiOiJBQ0NHS1g4N1lHWlNZVlBQIiwidmFsdWVUeXBlIjoiU0lOR0xFX1ZBTFVFRCJ9fSwidGl0bGUiOnsibXVsdGlWYWx1ZWRBdHRyaWJ1dGUiOnsia2V5IjoidGl0bGUiLCJpbmZlcmVuY2VUeXBlIjoiVElUTEUiLCJ2YWx1ZXMiOlsiS2V5Ym9hcmQgYW5kIENvbWJvcyJdLCJ2YWx1ZVR5cGUiOiJNVUxUSV9WQUxVRUQifX19fX0%3D&fm=neo%2Fmerchandising&iid=M_14ecc951-76f6-4e25-9063-f25d6e3bcd7f_1.FM7SOOTCJSU9&ppt=hp&ppn=homepage&ssid=zobm7qdl800000001744279673489&otracker=dynamic_omu_infinite_IT%2BAccessories_1_1.dealCard.OMU_INFINITE_FM7SOOTCJSU9&cid=FM7SOOTCJSU9"
#sending request to the url
#and getting the content of the page
contennt=requests.get(url)
soup=BeautifulSoup(contennt.content,"html.parser")


#creating empty lists to store the data
#that we are going to scrape
product_name=[]
price=[]
product_rate=[]
#finding the data using the class name
link=soup.findAll(["a"],class_="wjcEIp")

rate=soup.find_all(['div'],class_="_5OesEi afFzxY")

div=soup.find_all(["div"],class_="Nx9bqj")
#inserting the data into the lists
for  name,dive,rating in zip(link,div,rate):
    product_name.append(name.text.strip())
    price.append(dive.text.strip())
    product_rate.append(rating.text.strip())
    
#creating data for clean visualize using pandas
data={
    "product name":product_name,
    "price":price,
    "rating":product_rate
}

df=pd.DataFrame(data)
print(df.to_string(index=True))
