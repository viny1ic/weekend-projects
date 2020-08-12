from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


# driver= webdriver.Chrome()
driver = webdriver.Chrome(ChromeDriverManager().install())  # comment out this line if useing windows
driver.get('https://web.whatsapp.com')  # comment out this line if useing windows
# driver= webdriver.Chrome() #comment in this line if using windows

contact=input('enter name of your contact: ')
script=input('enter the script to spam: ')
msg=list(script.split())
input("if QR code is scanned then press enter, otherwise scan QR code")
user=driver.find_element_by_xpath('//span[@title="{}"]'.format(contact))
user.click()
msg_box = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div' )
for i in msg:
    msg_box.send_keys(i)
    # button=driver.find_element_by_class_name('_35EW6')
    # button.click()
    msg_box.send_keys(Keys.ENTER)
print('Done')