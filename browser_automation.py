from selenium import webdriver
import time
import csv
from selenium.webdriver.common.keys import Keys


firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference('permissions.default.image', 2)
firefox_profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
driver = webdriver.Firefox(firefox_profile=firefox_profile)
driver_new = webdriver.Firefox(firefox_profile=firefox_profile)
driver.get("https://www.inshorts.com/en/read")

def button_click(number,time):
    for i in range(number):
        try:
            Button = driver.find_element_by_id('load-more-btn')
            Button.click()
            print(i)
            time.sleep(time)
        except:
            continue
def add_to_csv(index,news_title,news_summary,source_name,news_article,link):
    with open('document.csv','a') as fd:
        writer = csv.writer(fd)
        writer.writerow([index,news_title,news_summary,source_name,news_article,link])

def get_from_techCrunch(link,index,news_title,news_summary,source_name):
    driver_new.get(link)
    # driver_new.find_element_by_class_name('exit-close').click()
    text = driver_new.find_element_by_class_name('article-content').find_elements_by_css_selector('p')
    l=[]
    for i in range(len(text)):
        print(text[i].get_attribute('textContent'))
        l.append(text[i].get_attribute('textContent'))


    article = ''.join(l)
    add_to_csv(index,news_title,news_summary,source_name,article,link)

def get_from_livemint(link,index,news_title,news_summary,source_name):
    driver_new.get(link)
    driver_new.find_element_by_class_name('btn_disagree').click()
    text = driver_new.find_element_by_class_name('mainArea').find_elements_by_css_selector('p')
    l = []
    for i in range(len(text)):
        print(text[i].get_attribute('textContent'))
        l.append(text[i].get_attribute('textContent'))

    article = ''.join(l)
    add_to_csv(index,news_title,news_summary,source_name,article,link)
    # print(text)

def get_from_timesnow(link,index,news_title,news_summary,source_name):
    driver_new.get(link)
    text = driver_new.find_element_by_class_name('artical-description').find_elements_by_css_selector('p')
    l = []
    for i in range(len(text)):
        print(text[i].get_attribute('textContent'))
        l.append(text[i].get_attribute('textContent'))


    article = ''.join(l)
    add_to_csv(index,news_title,news_summary,source_name,article,link)

def get_from_hindustantimes(link,index,news_title,news_summary,source_name):
    driver_new.get(link)
    time.sleep(5)
    driver_new.find_element_by_class_name('btn_disagree').click()
    text = driver_new.find_element_by_class_name('story-details').find_elements_by_css_selector('p')
    l = []
    for i in range(len(text)):
        if(i!=(len(text)-1) and i!=(len(text)-2)):
            print(text[i].get_attribute('textContent'))
            l.append(text[i].get_attribute('textContent'))
    article = ''.join(l)
    add_to_csv(index,news_title,news_summary,source_name,article,link)

def get_from_newindianexpress(link,index,news_title,news_summary,source_name):
    driver_new.get(link)
    text = driver_new.find_element_by_id('storyContent').find_elements_by_css_selector('p')
    l = []
    for i in range(len(text)):
        print(text[i].get_attribute('textContent'))
        l.append(text[i].get_attribute('textContent'))


    article = ''.join(l)
    add_to_csv(index,news_title,news_summary,source_name,article,link)

def get_from_guardian(link,index,news_title,news_summary,source_name):
    driver_new.get(link)
    text = driver_new.find_element_by_class_name('content__article-body').find_elements_by_css_selector('p')
    l = []
    for i in range(len(text)):
        print(text[i].get_attribute('textContent'))
        l.append(text[i].get_attribute('textContent'))


    article = ''.join(l)
    add_to_csv(index,news_title,news_summary,source_name,article,link)

def get_from_crictracker(link,index,news_title,news_summary,source_name):
    driver_new.get(link)
    text = driver_new.find_element_by_class_name('meta-content').find_elements_by_css_selector('p')
    l = []
    for i in range(len(text)):
        if(i!=(len(text)-1)):
            print(text[i].get_attribute('textContent'))
            l.append(text[i].get_attribute('textContent'))

    article = ''.join(l)
    add_to_csv(index,news_title,news_summary,source_name,article,link)

def get_from_indiacom(link,index,news_title,news_summary,source_name):
    driver_new.get(link)
    text = driver_new.find_element_by_class_name('articleBody').find_elements_by_css_selector('p')
    l = []
    for i in range(len(text)):
        print(text[i].get_attribute('textContent'))
        l.append(text[i].get_attribute('textContent'))

    article = ''.join(l)
    add_to_csv(index,news_title,news_summary,source_name,article,link)

def get_from_dailymail(link,index,news_title,news_summary,source_name):
    driver_new.get(link)
    text = driver_new.find_element_by_xpath('//*[@itemprop="articleBody"]').find_elements_by_css_selector('p')
    l = []
    for i in range(len(text)):
        print(text[i].get_attribute('textContent'))
        l.append(text[i].get_attribute('textContent'))

    article = ''.join(l)
    add_to_csv(index,news_title,news_summary,source_name,article,link)

def get_from_thenewsminute(link,index,news_title,news_summary,source_name):
    driver_new.get(link)
    text = driver_new.find_element_by_xpath('//*[@itemprop="articleBody"]').find_elements_by_css_selector('p')
    l = []
    for i in range(len(text)):
        print(text[i].get_attribute('textContent'))
        l.append(text[i].get_attribute('textContent'))

    article = ''.join(l)
    add_to_csv(index,news_title,news_summary,source_name,article,link)

def get_from_ani(link,index,news_title,news_summary,source_name):
    driver_new.get(link)
    text = driver_new.find_element_by_xpath('//*[@itemprop="articleBody"]').find_elements_by_css_selector('p')
    l = []
    for i in range(len(text)):
        print(text[i].get_attribute('textContent'))
        l.append(text[i].get_attribute('textContent'))

    article = ''.join(l)
    add_to_csv(index,news_title,news_summary,source_name,article,link)

def get_from_quint(link,index,news_title,news_summary,source_name):
    driver_new.get(link)
    text = driver_new.find_element_by_class_name('story-article__cards').find_elements_by_css_selector('.story-article__content__element--text p')
    l = []
    for i in range(len(text)):
        print(text[i].get_attribute('textContent'))
        l.append(text[i].get_attribute('textContent'))

    article = ''.join(l)
    add_to_csv(index,news_title,news_summary,source_name,article,link)

def get_from_bloombergquint(link,index,news_title,news_summary,source_name):
    driver_new.get(link)
    text = driver_new.find_element_by_class_name('paywall').find_elements_by_css_selector('p')
    l = []
    for i in range(len(text)):
        print(text[i].get_attribute('textContent'))
        l.append(text[i].get_attribute('textContent'))

    article = ''.join(l)
    add_to_csv(index,news_title,news_summary,source_name,article,link)

def get_from_inc42(link,index,news_title,news_summary,source_name):
    driver_new.get(link)
    text = driver_new.find_element_by_class_name('entry-content').find_elements_by_class_name('selectionShareable')
    l = []
    for i in range(len(text)):
        if(text[i].get_attribute('textContent').find("Related Article:") == -1):
            print(text[i].get_attribute('textContent'))
            l.append(text[i].get_attribute('textContent'))

    article = ''.join(l)
    add_to_csv(index,news_title,news_summary,source_name,article,link)

def get_from_reuters(link,index,news_title,news_summary,source_name):
    driver_new.get(link)
    text = driver_new.find_element_by_class_name('StandardArticleBody_body').find_elements_by_css_selector('p')
    l = []
    for i in range(len(text)):
        print(text[i].get_attribute('textContent'))
        l.append(text[i].get_attribute('textContent'))

    article = ''.join(l)
    add_to_csv(index,news_title,news_summary,source_name,article,link)

def get_from_financialexpress(link,index,news_title,news_summary,source_name):
    driver_new.get(link)
    text = driver_new.find_element_by_class_name('leftstory').find_elements_by_css_selector('p')
    l = []
    for i in range(len(text)):
        print(text[i].get_attribute('textContent'))
        l.append(text[i].get_attribute('textContent'))

    article = ''.join(l)
    add_to_csv(index,news_title,news_summary,source_name,article,link)

def get_from_rt(link,index,news_title,news_summary,source_name):
    driver_new.get(link)
    text = driver_new.find_element_by_class_name('article__text').find_elements_by_css_selector('p')
    l = []
    for i in range(len(text)):
        print(text[i].get_attribute('textContent'))
        l.append(text[i].get_attribute('textContent'))

    article = ''.join(l)
    add_to_csv(index,news_title,news_summary,source_name,article,link)

def get_from_freepressjournal(link,index,news_title,news_summary,source_name):
    driver_new.get(link)
    text = driver_new.find_element_by_class_name('story-element-text').find_elements_by_css_selector('p')
    l = []
    for i in range(len(text)):
        print(text[i].get_attribute('textContent'))
        l.append(text[i].get_attribute('textContent'))

    article = ''.join(l)
    add_to_csv(index,news_title,news_summary,source_name,article,link)

def get_from_thewire(link,index,news_title,news_summary,source_name):
    driver_new.get(link)
    text = driver_new.find_element_by_class_name('postComplete__description').find_elements_by_css_selector('p')
    l = []
    for i in range(len(text)):
        if(text[i].get_attribute('textContent').find("Also read:") == -1):
            print(text[i].get_attribute('textContent'))
            l.append(text[i].get_attribute('textContent'))

    article = ''.join(l)
    add_to_csv(index,news_title,news_summary,source_name,article,link)

def get_from_engadget(link,index,news_title,news_summary,source_name):
    driver_new.get(link)
    text = driver_new.find_element_by_id('page_body').find_elements_by_css_selector('.article-text p')
    l = []
    for i in range(len(text)):
        print(text[i].get_attribute('textContent'))
        l.append(text[i].get_attribute('textContent'))

    article = ''.join(l)
    add_to_csv(index,news_title,news_summary,source_name,article,link)

def get_from_vogueindia(link,index,news_title,news_summary,source_name):
    driver_new.get(link)
    text = driver_new.find_element_by_class_name('description').find_elements_by_css_selector('p')
    l = []
    for i in range(len(text)):
        print(text[i].get_attribute('textContent'))
        l.append(text[i].get_attribute('textContent'))

    article = ''.join(l)
    add_to_csv(index,news_title,news_summary,source_name,article,link)

def get_from_entrackr(link,index,news_title,news_summary,source_name):
    driver_new.get(link)
    text = driver_new.find_element_by_xpath('//*[@data-widget_type="theme-post-content.default"]').find_elements_by_css_selector('p')
    l = []
    for i in range(len(text)):
        print(text[i].get_attribute('textContent'))
        l.append(text[i].get_attribute('textContent'))

    article = ''.join(l)
    add_to_csv(index,news_title,news_summary,source_name,article,link)

def get_from_pti(link,index,news_title,news_summary,source_name):
    driver_new.get(link)
    text = driver_new.find_elements_by_class_name('fulstorytext')
    l = []
    for i in range(len(text)):
        print(text[i].get_attribute('textContent'))
        l.append(text[i].get_attribute('textContent'))

    article = ''.join(l)
    add_to_csv(index,news_title,news_summary,source_name,article,link)

def get_from_bollywoodhungama(link,index,news_title,news_summary,source_name):
    driver_new.get(link)
    text = driver_new.find_element_by_class_name('entry-content').find_elements_by_css_selector('p')
    l = []
    for i in range(len(text)):
        print(text[i].text)
        l.append(text[i].text)

    article = ''.join(l)
    add_to_csv(index,news_title,news_summary,source_name,article,link)

def get_from_pinkvilla(link,index,news_title,news_summary,source_name):
    driver_new.get(link)
    text = driver_new.find_element_by_id('ct1').find_elements_by_css_selector('p')
    l = []
    for i in range(len(text)):
        print(text[i].text)
        l.append(text[i].text)

    article = ''.join(l)
    add_to_csv(index,news_title,news_summary,source_name,article,link)

def get_from_cricketcountry(link,index,news_title,news_summary,source_name):
    driver_new.get(link)
    text = driver_new.find_element_by_class_name('cc-main-content').find_elements_by_css_selector('p')
    l = []
    for i in range(len(text)):
        print(text[i].text)
        l.append(text[i].text)

    article = ''.join(l)
    add_to_csv(index,news_title,news_summary,source_name,article,link)

def get_from_whitehouse(link,index,news_title,news_summary,source_name):
    driver_new.get(link)
    text = driver_new.find_element_by_class_name('page-content__content').find_elements_by_css_selector('p')
    l = []
    for i in range(len(text)):
        print(text[i].text)
        l.append(text[i].text)

    article = ''.join(l)
    add_to_csv(index,news_title,news_summary,source_name,article,link)

def get_from_yourstory(link,index,news_title,news_summary,source_name):
    driver_new.get(link)
    text = driver_new.find_element_by_class_name('quill-content').find_elements_by_css_selector('p')
    l = []
    for i in range(len(text)):
        print(text[i].text)
        l.append(text[i].text)

    article = ''.join(l)
    add_to_csv(index,news_title,news_summary,source_name,article,link)

def get_from_cricketaustralia(link,index,news_title,news_summary,source_name):
    driver_new.get(link)
    text = driver_new.find_element_by_class_name('news-content').find_elements_by_css_selector('p')
    l = []
    for i in range(len(text)):
        print(text[i].text)
        l.append(text[i].text)

    article = ''.join(l)
    add_to_csv(index,news_title,news_summary,source_name,article,link)

def get_from_ftc(link,index,news_title,news_summary,source_name):
    driver_new.get(link)
    text = driver_new.find_element_by_class_name('field-item').find_elements_by_css_selector('p')
    l = []
    for i in range(len(text)):
        print(text[i].text)
        l.append(text[i].text)

    article = ''.join(l)
    add_to_csv(index,news_title,news_summary,source_name,article,link)

def get_from_delhiplanet(link,index,news_title,news_summary,source_name):
    driver_new.get(link)
    text = driver_new.find_element_by_class_name('story-detail').find_elements_by_css_selector('p')
    l = []
    for i in range(len(text)):
        print(text[i].text)
        l.append(text[i].text)

    article = ''.join(l)
    add_to_csv(index,news_title,news_summary,source_name,article,link)

def get_from_phys(link,index,news_title,news_summary,source_name):
    driver_new.get(link)
    text = driver_new.find_element_by_class_name('article-main').find_elements_by_css_selector('p')
    l = []
    for i in range(len(text)):
        print(text[i].text)
        l.append(text[i].text)

    article = ''.join(l)
    add_to_csv(index,news_title,news_summary,source_name,article,link)

def get_from_pri(link,index,news_title,news_summary,source_name):
    driver_new.get(link)
    text = driver_new.find_element_by_class_name('node-story').find_elements_by_css_selector('p')
    l = []
    for i in range(len(text)):
        print(text[i].text)
        l.append(text[i].text)

    article = ''.join(l)
    add_to_csv(index,news_title,news_summary,source_name,article,link)

def get_from_bgr(link,index,news_title,news_summary,source_name):
    driver_new.get(link)
    text = driver_new.find_element_by_class_name('article-content').find_elements_by_css_selector('p')
    l = []
    for i in range(len(text)):
        print(text[i].text)
        l.append(text[i].text)

    article = ''.join(l)
    add_to_csv(index,news_title,news_summary,source_name,article,link)

def get_from_pnas(link,index,news_title,news_summary,source_name):
    driver_new.get(link)
    text = driver_new.find_element_by_class_name('pane-highwire-panel-tabs-container').find_elements_by_css_selector('p')
    l = []
    for i in range(len(text)):
        print(text[i].text)
        l.append(text[i].text)

    article = ''.join(l)
    add_to_csv(index,news_title,news_summary,source_name,article,link)

def get_from_purdue(link,index,news_title,news_summary,source_name):
    driver_new.get(link)
    text = driver_new.find_element_by_class_name('maincontent').find_elements_by_css_selector('p')
    l = []
    for i in range(len(text)):
        print(text[i].text)
        l.append(text[i].text)

    article = ''.join(l)
    add_to_csv(index,news_title,news_summary,source_name,article,link)

def get_from_techcircle(link,index,news_title,news_summary,source_name):
    driver_new.get(link)
    text = driver_new.find_element_by_class_name('article-content').find_elements_by_css_selector('p')
    l = []
    for i in range(len(text)):
        print(text[i].text)
        l.append(text[i].text)

    article = ''.join(l)
    add_to_csv(index,news_title,news_summary,source_name,article,link)

def get_from_spotboye(link,index,news_title,news_summary,source_name):
    driver_new.get(link)
    text = driver_new.find_elements_by_id('mvp-content-main')
    l = []
    for i in range(len(text)):
        print(text[i].text)
        l.append(text[i].text)

    article = ''.join(l)
    add_to_csv(index,news_title,news_summary,source_name,article,link)



def others():
    print('Null')

def get_from_source(link,index,news_title,news_summary):
    print(link.get_attribute('href'))
    print(link.text)
    if(link.text=='TechCrunch'||link.text=='Tech Crunch'):
        get_from_techCrunch(link.get_attribute('href'),index,news_title,news_summary,link.text)
    elif(link.text=='Livemint'):
        get_from_livemint(link.get_attribute('href'),index,news_title,news_summary,link.text)
    elif(link.text=='FTC'):
        get_from_ftc(link.get_attribute('href'),index,news_title,news_summary,link.text)
    elif(link.text=='Delhi Planet'):
        get_from_delhiplanet(link.get_attribute('href'),index,news_title,news_summary,link.text)
    elif(link.text=='Phys.org'):
        get_from_phys(link.get_attribute('href'),index,news_title,news_summary,link.text)
    elif(link.text=='PRI'):
        get_from_pri(link.get_attribute('href'),index,news_title,news_summary,link.text)
    elif(link.text=='BGR'||link.text=='BGR India'):
        get_from_bgr(link.get_attribute('href'),index,news_title,news_summary,link.text)
    elif(link.text=='PNAS'):
        get_from_pnas(link.get_attribute('href'),index,news_title,news_summary,link.text)
    elif(link.text=='TechCircle'):
        get_from_techcircle(link.get_attribute('href'),index,news_title,news_summary,link.text)
    elif(link.text=='Purdue University'):
        get_from_purdue(link.get_attribute('href'),index,news_title,news_summary,link.text)
    elif(link.text=='Times Now'):
        get_from_timesnow(link.get_attribute('href'),index,news_title,news_summary,link.text)
    elif(link.text=='Hindustan Times'):
        get_from_hindustantimes(link.get_attribute('href'),index,news_title,news_summary,link.text)
    elif(link.text=='The New Indian Express'):
        get_from_newindianexpress(link.get_attribute('href'),index,news_title,news_summary,link.text)
    elif(link.text=='The Guardian'):
        get_from_guardian(link.get_attribute('href'),index,news_title,news_summary,link.text)
    elif(link.text=='CricTracker'):
        get_from_crictracker(link.get_attribute('href'),index,news_title,news_summary,link.text)
    elif(link.text=='India.com'):
        get_from_indiacom(link.get_attribute('href'),index,news_title,news_summary,link.text)
    elif(link.text=='Daily Mail'):
        get_from_dailymail(link.get_attribute('href'),index,news_title,news_summary,link.text)
    elif(link.text=='The News Minute'):
        get_from_thenewsminute(link.get_attribute('href'),index,news_title,news_summary,link.text)
    elif(link.text=='ANI'||link.text=='ANI News'):
        if link.get_attribute('href').find("twitter.com") == -1:
            get_from_ani(link.get_attribute('href'),index,news_title,news_summary,link.text)
        else:
            others()
    elif(link.text=='The Quint'):
        get_from_quint(link.get_attribute('href'),index,news_title,news_summary,link.text)
    elif(link.text=='Bloomberg Quint'||link.text=='BloombergQuint'):
        get_from_bloombergquint(link.get_attribute('href'),index,news_title,news_summary,link.text)
    elif(link.text=='Inc42'):
        get_from_inc42(link.get_attribute('href'),index,news_title,news_summary,link.text)
    elif(link.text=='Reuters'):
        get_from_reuters(link.get_attribute('href'),index,news_title,news_summary,link.text)
    elif(link.text=='The Financial Express'||link.text=='Financial Express'):
        get_from_financialexpress(link.get_attribute('href'),index,news_title,news_summary,link.text)
    elif(link.text=='RT'):
        get_from_rt(link.get_attribute('href'),index,news_title,news_summary,link.text)
    elif(link.text=='Free Press Journal'||link.text=='The Free Press Journal'):
        get_from_freepressjournal(link.get_attribute('href'),index,news_title,news_summary,link.text)
    elif(link.text=='The Wire'):
        get_from_thewire(link.get_attribute('href'),index,news_title,news_summary,link.text)
    elif(link.text=='Engadget'):
        get_from_engadget(link.get_attribute('href'),index,news_title,news_summary,link.text)
    elif(link.text=='Vogue India'):
        get_from_vogueindia(link.get_attribute('href'),index,news_title,news_summary,link.text)
    elif(link.text=='Entrackr'):
        get_from_entrackr(link.get_attribute('href'),index,news_title,news_summary,link.text)
    elif(link.text=='SpotboyE'||link.text=='SpotBoyE'):
        get_from_spotboye(link.get_attribute('href'),index,news_title,news_summary,link.text)
    elif(link.text=='PTI'):
        get_from_pti(link.get_attribute('href'),index,news_title,news_summary,link.text)
    elif(link.text=='Bollywood Hungama'):
        get_from_bollywoodhungama(link.get_attribute('href'),index,news_title,news_summary,link.text)
    elif(link.text=='Pinkvilla'):
        get_from_pinkvilla(link.get_attribute('href'),index,news_title,news_summary,link.text)
    elif(link.text=='Cricket Country'):
        get_from_cricketcountry(link.get_attribute('href'),index,news_title,news_summary,link.text)
    elif(link.text=='The White House'):
        get_from_whitehouse(link.get_attribute('href'),index,news_title,news_summary,link.text)
    elif(link.text=='YourStory'):
        get_from_yourstory(link.get_attribute('href'),index,news_title,news_summary,link.text)
    elif(link.text=='Cricket Australia'):
        get_from_cricketaustralia(link.get_attribute('href'),index,news_title,news_summary,link.text)
    else:
        others()


def get_from_inshots():
    button_click(500,10)
    news = driver.find_elements_by_class_name('news-card')
    for i in range(len(news)):
        print(i)
        news_summary_title = news[i].find_element_by_class_name(
            'news-card-title').find_element_by_css_selector('a').text
        print(news_summary_title)
        news_summary = news[i].find_element_by_class_name('news-card-content').text
        print(news_summary)
        try:
            news_source = news[i].find_element_by_class_name('news-card-footer').find_element_by_css_selector('.read-more a')
            get_from_source(news_source,i,news_summary_title,news_summary)
        except:
            print('Null')
    driver.quit()
    driver_new.quit()

get_from_inshots()
# get_from_livemint('.')
# sumTitle = driver.find_elements_by_xpath('//*[@itemprop="headline"]')
# sumArticle = driver.find_elements_by_xpath(
#     '//*[@itemprop="articleBody"]')
# articleLink = driver.find_elements_by_xpath(
#     "//div[@class='read-more']//a[@class='source']")
# print(links.find_element_by_xpath('//div[@class="result results_links_deep highlight_d result--url-above-snippet"]'))

# try:
#     print(i)
#     print(sumTitle[i].text)
#     print(sumArticle[i].text)
#     print(articleLink[i].get_attribute('href'))
# except:
#     print('none')

# find_element_by_xpath('//div[@class="result results_links_deep highlight_d result--url-above-snippet"]')
