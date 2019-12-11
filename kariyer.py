import sqlite3
import time
import re
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.webdriver import FirefoxProfile

profile = FirefoxProfile("C:\\Users\\gokha\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\b21rnkyt.kariyer")
profile.add_extension(r'C:\\Users\\gokha\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\b21rnkyt.kariyer\\extensions\\adblock.xpi') # for adblockplus
profile.set_preference("extensions.adblockplus.currentVersion","3.7")
binary = FirefoxBinary("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
browser = webdriver.Firefox(firefox_profile=profile, firefox_binary=binary)
browser.maximize_window()
sayfano = 0
linkler = []
durum = "0"
conn = sqlite3.connect('veritaban.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS basvurulinkleri(urll TEXT,durumu TEXT)')

def giris_yap():
    kullanıcı_adı = input()
    sifre = input()
    browser.get("https://www.kariyer.net/website/kariyerim/login.aspx")
    time.sleep(3)
    username = browser.find_element_by_xpath("//*[@id='lgnUserName']")
    password = browser.find_element_by_xpath("//*[@id='lgnPassword']")
    username.send_keys(kullanıcı_adı)
    password.send_keys(sifre)


browser.get("https://www.kariyer.net/is-ilanlari")
browser.execute_script(("document.body.style.zoom='15 %'"))
time.sleep(3)
sayfano = browser.find_element_by_xpath("//*[@id='lnkLastPage']").text
sayfano = int(re.search(r'\d+', sayfano).group())



def ilanlari_tara():
    elements = browser.find_elements_by_css_selector(".col-9")

    # for element in elements:
    #
    #   # # print(element.find_element_by_css_selector("a").get_attribute("href"))
    #   #   element = element.find_element_by_css_selector("a").get_attribute("href")
    #   #
    #   #
    #   #   # durum = "1"
    #   #   # c.execute('INSERT INTO basvurulinkleri (urll, durumu) VALUES(?,?)', (element, durum))
    #   #   # conn.commit()
    liste53 = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]

    for i in liste53:
        a = "/html/body/main/div/div[2]/div/div/div[3]/div[2]/div["
        b = "]/div/div[2]/p[1]/a"
        c = str(i)
        d = a + c + b
        time.sleep(1)

        try:
            ilan = browser.find_element_by_xpath(d)
            browser.execute_script("arguments[0].scrollIntoView({block: 'center'})", ilan)
            ilan.click()
            time.sleep(3)
            browser.switch_to.window(browser.window_handles[1])
            basvur()
            browser.close()
            time.sleep(1)
            browser.switch_to.window(browser.window_handles[0])
        except Exception:
            pass





def sadelestir():
    matching = [s for s in linkler if "kariyer" in s]

def sonraki():

    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(1)
    sayfadegistir = browser.find_element_by_xpath("/html/body/main/div/div[2]/div/div/div[5]/a[3]")
    time.sleep(1)
    sayfadegistir.click()

def basvur():

    t=str(5)

    # browser.get("https://www.kariyer.net/is-ilanlari/muhendislik")
    # c.execute("SELECT * FROM basvurulinkleri WHERE rowid = ? ", t)
    #
    # list = c.fetchone()
    #
    # url = ''.join(list)
    # print(url)
    #
    #
    # browser.find_element_by_link_text(url).click()
    time.sleep(1)
    try:
        ilanagit = browser.find_element_by_xpath("//*[@id='btnJobApply']")
        ilanagit.click()
        time.sleep(1)
    except Exception:
        pass

    try:
        tıkla3 = browser.find_element_by_xpath("/html/body/main/div/div[2]/form/div[2]/div/div/div[2]/div[1]/div").click()
    except Exception:
        pass

    try:

        onyazisec = browser.find_element_by_xpath("//*[@id='formBasvuruIcerik']/div[1]/div[2]/div[2]/div/label")
        onyazisec.click()
        time.sleep(1)
        onyazisec2 = browser.find_element_by_xpath("/html/body/div[5]/ul/li[5]")
        onyazisec2.click()
        time.sleep(2)
    except Exception:
        pass
    try:
        sehir1 = browser.find_element_by_xpath("//*[@id='formBasvuruIcerik']/div[2]/div[1]/div[2]/div/div/label")
        sehir1.click()
        browser.find_element_by_xpath("/html/body/div[6]/ul/li[1]").click()

    except Exception:
        pass
    time.sleep(1)
    try:
        sehir2 = browser.find_element_by_xpath("//*[@id='formBasvuruIcerik']/div[2]/div[2]/div[2]/div/div/label")
        sehir2.click()
        browser.find_element_by_xpath("/html/body/div[7]/ul/li[1]").click()
    except Exception:
        pass
    time.sleep(1)
    try:
        sehir3 = browser.find_element_by_xpath("//*[@id='formBasvuruIcerik']/div[2]/div[3]/div[2]/div/div/label")
        sehir3.click()
        browser.find_element_by_xpath("/html/body/div[8]/ul/li[1]").click()
    except Exception:
        pass


    try:
        basvurutamamla = browser.find_element_by_xpath("//*[@id='btnBasvuruTamamla']")
        basvurutamamla.click()

        c.execute("UPDATE basvurulinkleri SET durumu = ? WHERE rowid = ?", (2, t))
        conn.commit()


    except Exception:
        pass


a = 0

while a < sayfano :
    a = a+1

    ilanlari_tara()
    sonraki()
    time.sleep(2)