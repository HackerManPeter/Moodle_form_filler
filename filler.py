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

    moodle_login(os.environ.get('MOODLE_USERNAME'), os.environ.get('MOODLE_PASSWORD')) # Enter your username and password for the moodle sites as a string

    course_url = 'https://moodle.covenantuniversity.edu.ng/mod/feedback/complete.php?id=43637&courseid='
    

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

        if '43637' in course_id:
            course_id.remove('43637')

    driver.get(course_url+course_id[0])
    values = [2,3,3,2,2,3,3,2,2,2,2,3,3,3,2,3,3,2,2,3,2,3,3,2,3,3,2,3,2,3]
 
        


    # Loops through course via course id
    for id in course_id:
        driver.get(course_url+id)
        index = 0
        selectors = driver.find_elements_by_class_name('custom-select')
        for element in selectors:
            element_id = element.get_attribute('id')
            select = Select(driver.find_element_by_id(element_id))
            try:
                select.select_by_index(values[index])
            except:
                break
            index+=1
        try:    
            lecturer_name = driver.find_element_by_id('id_textfield_390')
        except:
            continue
        lecturer_name.send_keys("Null")
        driver.find_element_by_id('id_savevalues').click()

        
   



if __name__ == '__main__':
    main()