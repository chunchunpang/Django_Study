 # -*- coding: utf-8 -*- 
from selenium import webdriver

import pymysql

db=pymysql.connect("localhost","root","","mydb",charset='utf8')
cursor = db.cursor()

cursor.execute("drop table if exists myweb_music")
sql="""create table myweb_music(
                id INT AUTO_INCREMENT,
		title_name text,
		#num int unsigned,
		num text,
		link text,
		PRIMARY KEY ( id )) default charset=utf8
	"""
cursor.execute(sql)
db.close()

def insertdata(sql):
	db=pymysql.connect("localhost","root","","mydb",charset='utf8')
			
	cursor = db.cursor()
	
	try:
                cursor.execute(sql)
                db.commit()
	except:
                db.rollback()
	db.close()

url='http://music.163.com/#/discover/playlist'

options = webdriver.FirefoxOptions()
options.set_headless()
options.add_argument('--disable-gpu')
driver=webdriver.Firefox(firefox_options=options)


while url!='javascript:void(0)':
    driver.get(url)
    driver.switch_to.frame("contentFrame")
    data=driver.find_element_by_id("m-pl-container").find_elements_by_tag_name("li")
    for i in range(len(data)):
        nb=data[i].find_element_by_class_name("nb").text
	
        if '万' in nb and int(nb.split('万')[0])>500:			
            msk=data[i].find_element_by_css_selector("a.msk")
            title=msk.get_attribute('title')#.encode("utf-8",'ignore')
            link=msk.get_attribute('href')#.encode("utf-8",'ignore')
            nb=nb#.encode("utf-8",'ignore')
            #print(nb)
            sql="""insert into myweb_music(title_name,num,link) values
                (\""""+title+"""\",\"
                """+nb+"""\",\""""+link+"""\")"""
            #print (sql)
            #print (type(sql))
            insertdata(sql)
    url=driver.find_element_by_css_selector("a.zbtn.znxt").get_attribute('href')


