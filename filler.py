# A script that automatically fills course evaluation form on the Covenant University moodle platform
# for each course using selenium 
import os
import re
from selenium.webdriver import Firefox  
from selenium.webdriver.support.ui import Select

driver = Firefox()





def moodle_login(username, password):
    '''
    Logs you into covenant university moodle platform with the username and password provided
    '''
    driver.get("https://moodle.covenantuniversity.edu.ng/login/index.php")
    username_field = driver.find_element_by_id("username")
    password_field = driver.find_element_by_id("password")
    login = driver.find_element_by_id("loginbtn")

    username_field.send_keys(username)
    password_field.send_keys(password)
    login.click()

def main():
    
    '''
    main
    '''

    moodle_login(os.environ.get('USERNAME'), os.environ.get('PASSWORD')) # Enter your username and password for the moodle sites as a string

    course_url = 'https://moodle.covenantuniversity.edu.ng/mod/feedback/complete.php?id=43258&courseid='


    # Gets course_id for each course you are registered for 
    elements = driver.find_elements_by_class_name('aalink')
    course_id = list()
    for link in elements:
        course_href = link.get_attribute('href')
        try:
            item = re.search('id=([0-9].+)', course_href).group(1)
        except:
            continue
        course_id.append(item)

        if '43258' in course_id:
            course_id.remove('43258')

    

    # Loops through course via course id
    for id in course_id:
        driver.get(course_url+id)

        # Checks to see if evaluation for this course has already been filled 
        try:
            select  = Select(driver.find_element_by_id('id_multichoice_306'))
        except:
            continue
        select.select_by_visible_text('Agree')
        select  = Select(driver.find_element_by_id('id_multichoice_307'))
        select.select_by_visible_text('Disagree')
        select  = Select(driver.find_element_by_id('id_multichoice_309'))
        select.select_by_visible_text('Disagree')
        select  = Select(driver.find_element_by_id('id_multichoice_310'))
        select.select_by_visible_text('Agree')
        select  = Select(driver.find_element_by_id('id_multichoice_312'))
        select.select_by_visible_text('Agree')
        select  = Select(driver.find_element_by_id('id_multichoice_313'))
        select.select_by_visible_text('Disagree')
        select  = Select(driver.find_element_by_id('id_multichoice_336'))
        select.select_by_visible_text('Disagree')
        select  = Select(driver.find_element_by_id('id_multichoice_314'))
        select.select_by_visible_text('Agree')
        select  = Select(driver.find_element_by_id('id_multichoice_337'))
        select.select_by_visible_text('Agree')
        select  = Select(driver.find_element_by_id('id_multichoice_316'))
        select.select_by_visible_text('Agree')
        select  = Select(driver.find_element_by_id('id_multichoice_317'))
        select.select_by_visible_text('Agree')
        select  = Select(driver.find_element_by_id('id_multichoice_318'))
        select.select_by_visible_text('Disagree')
        select  = Select(driver.find_element_by_id('id_multichoice_320'))
        select.select_by_visible_text('Disagree')
        select  = Select(driver.find_element_by_id('id_multichoice_338'))
        select.select_by_visible_text('Disagree')
        select  = Select(driver.find_element_by_id('id_multichoice_321'))
        select.select_by_visible_text('Agree')
        select  = Select(driver.find_element_by_id('id_multichoice_339'))
        select.select_by_visible_text('Disagree')
        select  = Select(driver.find_element_by_id('id_multichoice_324'))
        select.select_by_visible_text('Disagree')
        select  = Select(driver.find_element_by_id('id_multichoice_323'))
        select.select_by_visible_text('Agree')
        select  = Select(driver.find_element_by_id('id_multichoice_326'))
        select.select_by_visible_text('Agree')
        select  = Select(driver.find_element_by_id('id_multichoice_327'))
        select.select_by_visible_text('Disagree')
        select  = Select(driver.find_element_by_id('id_multichoice_329'))
        select.select_by_visible_text('Agree')
        select  = Select(driver.find_element_by_id('id_multichoice_340'))
        select.select_by_visible_text('Disagree')
        select  = Select(driver.find_element_by_id('id_multichoice_330'))
        select.select_by_visible_text('Disagree')
        select  = Select(driver.find_element_by_id('id_multichoice_342'))
        select.select_by_visible_text('Agree')
        select  = Select(driver.find_element_by_id('id_multichoice_343'))
        select.select_by_visible_text('Disagree')
        select  = Select(driver.find_element_by_id('id_multichoice_345'))
        select.select_by_visible_text('Disagree')
        select  = Select(driver.find_element_by_id('id_multichoice_346'))
        select.select_by_visible_text('Agree')
        select  = Select(driver.find_element_by_id('id_multichoice_332'))
        select.select_by_visible_text('Disagree')
        select  = Select(driver.find_element_by_id('id_multichoice_333'))
        select.select_by_visible_text('Agree')

        lecturer_name = driver.find_element_by_id('id_textfield_347')
        lecturer_name.send_keys("Null")

        select  = Select(driver.find_element_by_id('id_multichoice_335'))
        select.select_by_visible_text('Good')

        submit = driver.find_element_by_id('id_savevalues')
        submit.click()
        





if __name__ == '__main__':
    main()