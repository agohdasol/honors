  
from selenium import webdriver
from bs4 import BeautifulSoup as bs
# 메일 로그인 주소
search_url = "https://www.mk.co.kr/news/all/"
# 크롬드라이버 위치
path = 'chromedriver.exe'
# 크롬드라이버 세팅
options = webdriver.ChromeOptions()
# 크롬드라이버 invisible 옵션
# options.add_argument('headless')
# options.add_argument('window-size=1920x1080')
# options.add_argument("disable-gpu")
# 크롬드라이버 실행
# driver = webdriver.Chrome(path, chrome_options=options)
driver = webdriver.Chrome(path)
driver.get(search_url)
driver.implicitly_wait(3)

# 크롤링
for page in [1, 2]:
    soup = bs(driver.page_source, 'html.parser')
    wow = soup.select('div#container > div#container_left > div.list_area > dl > dt.tit')
    for n in wow:
        print(n.text)

    driver.get("https://www.mk.co.kr/news/all/?page={}&thisDate=20200506".format(page))

driver.close()
