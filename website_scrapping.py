from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time,re
url="https://ful.io/"
driver=webdriver.Chrome(executable_path=r"")#give your own webdriver path
driver.maximize_window()
driver.get(url)
time.sleep(5)
social_links=[]
c=""
email=0
elems = driver.find_elements(By.XPATH,"//a[@href]")
for elem in elems:
    s=elem.get_attribute("href")
    obj1 = re.findall('([\w\-\.]+)',s)
    if(obj1[1]=="www.linkedin.com") or (obj1[1]=="www.facebook.com"):
        social_links.append(s)
    if obj1[1]=="support":
        email=str(obj1[1]+obj1[2])
    if obj1[0]=="tel":
       c="+"+" ".join(obj1[1:])
driver.close()
print("Social links -")
print(social_links[0])
print(social_links[1])
print("Email/s")
print(email)
print("Contact:")
print(c)


