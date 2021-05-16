import time
import telebot                                                                         #pip install pyTelegramBotAPI
from selenium import webdriver                                                         #pip install selenium 
from webdriver_manager.chrome import ChromeDriverManager                               #installare chrome driver piu aggiornati tramite questo link https://chromedriver.chromium.org/
from selenium.common.exceptions import NoSuchElementException #<-----------------------inserire questa eccezione nelle librerie
API_TOKEN = 'INSERISCI IL TUO TOKEN'                                                   #inserire il token telegram bot
bot = telebot.TeleBot(API_TOKEN)                                                       #pip install webdriver-manager
@bot.message_handler(func=lambda message: True)                                        #assicurarsi di avere un account SiteStripe(gratuito) con amazon
def echo_message(message):
    string = str(message.text)
    if "https://www.amazon.it/" in string.lower():
        options = webdriver.ChromeOptions()
        options.headless = True 
        options.add_argument("user-data-dir=C:INSERISCI IL PERCORSO CHROME")                                   # inserire il perocrso profilo puoi trovarlo digitando questo: "chrome//:version" sulla barra di ricerca
        w = webdriver.Chrome(executable_path="PERCORSO INSTALLAZIONE DRIVER CHROME", chrome_options=options)   # inserire prcorso file chrome driver  installati driver.exe
        w.get(string)
        try:                              
            if w.find_element_by_xpath("//div[@class='olp-text-box']").is_displayed():
                a = w.find_element_by_xpath("//*[@id='priceblock_ourprice']").text
                b = a.replace(",", ".")
                c = b.replace("€"," ")
                d = float(c)
                offersPanel = w.find_element_by_xpath("//div[@class='olp-text-box']").click()
                time.sleep(3.0)
                filterList = w.find_element_by_xpath("//*[@id='aod-filter-component']").click()
                freeShipping = w.find_element_by_xpath("//*[@id='freeShipping']").click()
                new = w.find_element_by_xpath("//*[@id='new']").click()
                if w.find_element_by_xpath("//*[@id='aod-price-1']").is_displayed():
                    e = w.find_element_by_xpath("//*[@id='aod-price-1']").text
                    f = e.replace("\n", ".")
                    g = f.replace("€"," ")
                    h = float(g)
                    if h < d:          
                        elem4 = w.find_element_by_xpath("//*[@id='aod-filter-component']").click()
                        aggiungialcarrello = w.find_element_by_xpath('(//*[@id="a-autoid-2"])[3]').click()
                        aggiungialcarrello1 = w.find_element_by_xpath("//*[@id='hlb-view-cart']").click()
                        aggiungialcarrello2 = w.find_element_by_xpath("//span[@class='a-size-medium a-color-base sc-product-title']").click()
                        w.switch_to.window(w.window_handles[-1])
                        titolo = w.find_element_by_xpath("//a[@title='Testo']").click()
                        time.sleep(3.0)
                        link = w.find_element_by_xpath("//*[@id='amzn-ss-text-shortlink-textarea']")
                        bot.reply_to(message, link.text) 
                        w.quit()
                    else:
                        w.quit()    #in caso di: offerta svantaggiosa
        except NoSuchElementException:
             bot.reply_to(message, "nessuna offerta trovata")   #in caso di: nessuna offerta trovata
    else:
        bot.reply_to(message, "link amazon errato")   #in caso di:  link errato 
bot.polling()
