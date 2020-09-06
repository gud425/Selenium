#-*- coding:utf-8 -*-
import time
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime

link="https://uportal.catholic.ac.kr/stw/scsr/scoo/scooLessonApplicationStudentReg.do"
myid="__id___"
mypassword="___pw___"
timeover_h=17
timeover_m=0

driver = webdriver.Chrome('C:\selenium\chromedriver_win32\chromedriver')
driver.get(link);
time.sleep(1)
def login(myid,mypassword):
    elem_login = driver.find_element_by_id("userId")
    elem_login.clear()
    elem_login.send_keys(myid)
    elem_login = driver.find_element_by_id("password")
    elem_login.clear()
    elem_login.send_keys(mypassword)
    xpath="""/html/body/div/form/div/div/div[1]/dl/dd[3]/button"""
    driver.find_element_by_xpath(xpath).click()
    time.sleep(5)
    #비밀번호 변경
    xpath="""//*[@id="jsrCommonPopup"]/section/div/div/div[3]/div/div/ul/li[1]/button"""
    driver.find_element_by_xpath(xpath).click()
    #학사정보
    time.sleep(3)
    driver.execute_script("javascript:$.header.clickMainMenu('2', 'C00040002', '/stw/main/noti/mainNoti.do', 'TRUE', $(this));")
    time.sleep(3)
    driver.execute_script("javascript:$.commonMenu.changeMenu('/scsr/scoo/scooLessonApplicationStudentReg.do');")

def crawling(index,soup):
    try:
        jehan = soup.select('#jsrBasketGrid > tr:nth-child('+str(index)+') > td:nth-child(8)')
        now = soup.select('#jsrBasketGrid > tr:nth-child('+str(index)+') > td:nth-child(9)')
        jehan=jehan[0].get_text()
        now=now[0].get_text()
        if(int(now)<int(jehan)):
            return True
        return False
    except:
        pass

def play(timeover_h,timeover_m):
    flag1=0
    flag2=0
    while(True):
        time.sleep(2)
        now=datetime.now()
        if(now.hour>=timeover_h and now.minute>=timeover_m):
            print("종료!")
            break
        driver.execute_script("location.reload()")
        time.sleep(1)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        
        if(flag1==0 and crawling(6,soup)):
            xpath="""//*[@id="jsrBasketGrid"]/tr[6]/td[13]/button"""
            driver.find_element_by_xpath(xpath).click()
            flag1=1
            print("과목먹었다옹")
        if(flag2==0 and crawling(5,soup)):
            xpath="""//*[@id="jsrBasketGrid"]/tr[5]/td[13]/button"""
            driver.find_element_by_xpath(xpath).click()
            flag2=1
            print("과목먹었다옹")
        if(flag1==1 and flag2==1):
            break
        
login(myid,mypassword)
play(timeover_h,timeover_m)

