# 크롤링 라이브러리 로드
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
# 엑셀 직접실행용
import win32com.client as win32
import time
import requests
import urllib


# 반복 정의
def execute_crawling():
    # 엑셀 실행-------------------------------------------------------------------------------------------------
    # excel = win32.Dispatch("Excel.Application")
    # excel.Visible = True    # 엑셀창 보이게
    
    # 크롬 헤드리스 설정(크롬창 안띄우게)-------------------------------------------------------------------------------------------------
    options = webdriver.ChromeOptions()
    #options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    # 크롬 드라이버 객체 생성
    driver = webdriver.Chrome('C:\Chrome Driver\chromedriver.exe', options=options)
    # 웹 자원 로드를 위해 3초 대기
    driver.implicitly_wait(1)
    # url에 접근
    driver.get('https://www.exportvoucher.com/portal/menupan/menu')
    driver.implicitly_wait(2)
    

    # 서비스 선택 - 일반 - 조사/일반 컨설팅
    # driver.find_element_by_xpath('//*[@id="contents"]/div/div[1]/ul/div[5]/li/a').click()
    # driver.implicitly_wait(0.5)
    # 서비스 선택 - 일반 - 특허/지재권/시험
    driver.find_element_by_xpath('//*[@id="contents"]/div/div[1]/ul/div[13]/li/a').click()
    driver.implicitly_wait(1)
    # 엑셀에 입력 반복문(메일 하나씩 반복체킹해서 입력)
    anitem = 1  # 상품 하나
    for page_check in range(1,49):    #페이지
        # 아이템 하나씩 클릭
        for n in range(1,25):
            try:
                driver.find_element_by_xpath('//*[@id="contents"]/div/div[3]/div[2]/table/tbody/tr[{}]/td[2]/p[1]/a'.format(anitem)).click()
                driver.implicitly_wait(1)
            except:
                try:
                    driver.implicitly_wait(1)
                    driver.find_element_by_xpath('//*[@id="contents"]/div/div[3]/div[2]/table/tbody/tr[{}]/td[2]/p[1]/a'.format(anitem)).click()
                    driver.implicitly_wait(1)
                except:
                    pass
            else:
                for nn in range(1,11):   # 첨부파일 모두 다운로드. 최대 10개까지 시도
                    try:
                        driver.find_element_by_xpath('//*[@id="aform"]/div[1]/div[4]/dl/dd/a[{}]'.format(nn)).click()
                        driver.implicitly_wait(3)
                    except:
                        break
                anitem = anitem + 1
                # 뒤로가기
                driver.back()
        # 더보기 클릭
        try:
            driver.find_element_by_xpath('//*[@id="contents"]/div/div[3]/div[2]/p/button').click()
        except:
            break
        driver.implicitly_wait(1)


execute_crawling()
