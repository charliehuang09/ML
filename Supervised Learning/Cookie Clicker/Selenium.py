from selenium import webdriver
from selenium.webdriver import *
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import warnings
warnings.filterwarnings("ignore")
options = ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--mute-audio")
Path = '/Users/charlie/Downloads/chromedriver_mac_arm64/chromedriver'
driver = webdriver.Chrome(chrome_options = options, executable_path = Path)
driver.get("https://orteil.dashnet.org/cookieclicker/")
language = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.ID, 'langSelect-EN')))
language.click()
print('languange clicked')

def goldenCookie():
    try:
        goldenCookie = driver.find_element_by_class_name('shimmer')
        goldenCookie.click()
    except:
        pass

def click(iterations = 1):
    for i in range(iterations * 2):
        time.sleep(1/1000)
        try:
            cookie = driver.find_element_by_id('bigCookie')
            cookie.click()
            goldenCookie()
        except:
            pass

def buildingUpgrade():
    buildings = driver.find_elements_by_class_name('enabled')
    for building in buildings:
        try:    
            building.click()
        except:
            pass

def passiveUpgrade():
    upgrades = [driver.find_element_by_id('upgrades')]
    for upgrade in upgrades:
        upgrade.click()

def upgrade():
    upgrades = driver.find_elements_by_class_name('enabled')
    upgrades.reverse()
    for upgrade in upgrades:
        try:
            upgrade.click()
        except:
            pass
    
def save():
    try:
        options = driver.find_element_by_id('prefsButton')
        options.click()
        exportSave = driver.find_element_by_xpath('/html/body/div/div[2]/div[18]/div[2]/div[4]/div[3]/div/div[4]/a[1]')
        exportSave.click()
        print('afd')
        save = driver.find_element_by_xpath('/html/body/div/div[2]/div[12]/div/div[1]/div[1]/div[2]/textarea').get_attribute('value')
        print(save)
        savefile = open("save.txt", "w")
        savefile.write(save)
        savefile.close()
        close1 = driver.find_element_by_xpath('/html/body/div/div[2]/div[12]/div/div[2]')
        close1.click()
        time.sleep(0.01)
        close2 = driver.find_element_by_xpath('/html/body/div/div[2]/div[18]/div[2]/div[4]/div[1]')
        close2.click()
    except:
        pass
    
temp = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.ID, 'bigCookie')))
print('loaded')
temp = input('start?')
while True:
    click(5000)
    # buildingUpgrade()
    # passiveUpgrade()
    #upgrade()
    #goldenCookie()
    save()
    
    
    
    