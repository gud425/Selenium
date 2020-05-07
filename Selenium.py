#-*- coding:utf-8 -*-
import time
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup

link="http://www.saramin.co.kr/zf_user/search?search_area=main&search_done=y&search_optional_item=n&searchType=default_mysearch&searchword=%EB%B3%B4%EC%B6%A9%EC%97%AD&loc_mcd=101000&cat_cd=404%2C402%2C411%2C407%2C408&cat_key=80906"

driver = webdriver.Chrome('C:\selenium\chromedriver_win32\chromedriver')
driver.get(link);
time.sleep(1)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
past_job=pd.read_csv('./job_info.txt',sep=',')


title=soup.select('h2[class="job_tit"]>a>span')
company_name=soup.select('strong[class="corp_name"]>a>span')
date=soup.select('div[class="job_date"]>span')
condition=soup.select('div[class="job_condition"]>span')

job_info=[]
cnt=1
for item in zip(title,company_name,date,condition):
    job_info.append(
            {
                'title':item[0].text,
                'company_name':item[1].text,
                'date':item[2].text,
                'condition':item[3].text
            }
        )
    if(past_job['title']!=item[0].text).all():
        new_job=driver.find_element_by_xpath('//*[@id="recruit_info_list"]/div[1]/div['+str(cnt)+']/div[1]/h2/a')
        new_job.click()
    cnt+=1

data=pd.DataFrame(job_info)


print(data)
data.to_csv('job_info.txt')


