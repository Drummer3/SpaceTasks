from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def firstStage():
    print('-'*5,'First Stage','-'*5)
    navigator = driver.find_element_by_class_name('WQFPo')
    navigatorsList = ['სერვისები', 'გადარიცხვები',
                      'ბიზნესისთვის', 'გადაიხადე უცხოეთიდან']
    i = navigator.get_attribute('innerHTML')
    for word in navigatorsList:
        if word in i:
            print('YES',word)
        else:
            print('NO', word)

    services = driver.find_element_by_class_name('kLtDrh')
    servicesList = ['პოპულარული სერვისები', 'მობილური კავშირი', 'ბანკები დაზღვევა მიკროსაფინანსო', 'ტოტალიზატორები კაზინო ლატარია',
                    'ინტერნეტი ტელეფონი ტელევიზია', 'კომუნალური გადახდები', 'ტრანსპორტი', 'სახელმწიფო სერვისები', 'სხვადასხვა']
    searchZone = services.get_attribute('innerHTML')
    for each in servicesList:
        if each in searchZone:
            print('YES',each)
        else:
            print('NO', each)
    
    time.sleep(2)
    driver.save_screenshot('images/FirstStage.png')
    try:
        search = driver.find_element_by_class_name('search-wrapper')
    except:
        print('საძიებო ველი ვერ მოიძებნა')
        return 0
    return 1

def secondStage():
    print('-'*5,'Second Stage','-'*5)
    search = driver.find_element_by_name("searchWord")
    search.clear()
    search.send_keys("მობილური")

    searchResult = driver.find_elements_by_class_name('fPqRiF')
    for each in searchResult:
        if each.text == "მობილური ბალანსის შევსება":
            time.sleep(1)
            driver.save_screenshot('images/SecondStage.png')
            thirdStage(each)
            break

def thirdStage(each):
    print('-'*5,'Third Stage','-'*5)
    each.click()
    time.sleep(1)
    driver.save_screenshot('images/ThirdStage.png')
    numberInput = driver.find_element_by_name('1213-abonentCode')
    numberSearch = driver.find_element_by_class_name('laXiIz')
    fourthStage(numberInput,numberSearch)
        
def fourthStage(numberInput,numberSearch):
    print('-'*5,'Fourth Stage','-'*5)
    numberInput.clear()
    numberInput.send_keys('555122334')
    numberSearch.click()
    time.sleep(1)
    driver.save_screenshot('images/FourthStage.png')
    fifthStage()

def fifthStage():
    print('-'*5,'Fifth Stage','-'*5)
    chooseService = driver.find_element_by_class_name('jBoyDl')
    chooseService.click()
    options = driver.find_elements_by_class_name('kpIxhG')
    taskData = ['ბალანსის შევსება','"მეტი" - 8 ₾','"მეტი" - 10 ₾']
    websiteData = []
    for option in options:
        if option.text == '"მეტი" - 10 ₾':
            nextStageData = option
        websiteData.append(option.text)
    for task in taskData:
        if task in websiteData:
            continue
        else:
            print(f'{task} არ არის საიტზე')
    time.sleep(1)
    driver.save_screenshot('images/FifthStage.png')
    stageSix(nextStageData)

def stageSix(button):
    print('-'*5,'Sixth Stage','-'*5)
    button.click()
    text = ['დავალიანება', '10.00 c', 'თანხის ოდენობა c', 'საკომისიო 0.12 c', 'ჯამში გადასახდელი', '10.12 c']
    time.sleep(2)
    zone = driver.find_element_by_class_name('iiRqkB')
    for each in text:
        if each in zone.get_attribute('innerHTML'):
            print('YES', each)
        else:
            print('NO', each)
    driver.save_screenshot('images/SixthStage.png')
    pay = zone.find_element_by_class_name('goRuDt')
    stageSeven(pay)

def stageSeven(pay):
    print('-'*5,'Seventh Stage','-'*5)
    pay.click()
    time.sleep(3)
    url = driver.current_url
    if 'ecommerce.ufc.ge' in url:
        print('წარმატებით გადამისამართდა')
    else:
        print('გადამისამართებისას ხარვეზი დაფიქსირდა')
    driver.save_screenshot('images/SeventhStage.png')


driver = webdriver.Chrome('chromedriver')
driver.maximize_window()
driver.get("https://tbcpay.ge/")

firstStep = firstStage()
if firstStep:
    secondStage()

driver.close()
