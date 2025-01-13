from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time



def userAuth(username, password) -> None:
    emailBox = driver.find_element(By.ID, "pseudonym_session_unique_id")
    passwordBox = driver.find_element(By.ID, "pseudonym_session_password")
    emailBox.click()
    emailBox.send_keys(username)
    passwordBox.click()
    passwordBox.send_keys(password)
    
    login = driver.find_element(By.CSS_SELECTOR, ".Button.Button--login")
    login.click()
    driver.implicitly_wait(100)
    

def getCourses(username, password) -> None:
    userAuth(username, password)
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".ic-DashboardCard")))
    
    courses = driver.find_elements(By.CSS_SELECTOR, ".ic-DashboardCard")
    
    for course in courses:
        try:

            courseContainer = WebDriverWait(course, 10).until(EC.presence_of_element_located((By.XPATH, ".//a[contains(@class, 'ic-DashboardCard__link')]")))
            courseURL = courseContainer.get_attribute("href")
            courseName = courseContainer.find_element(By.XPATH, ".//h3[contains(@class, 'ic-DashboardCard__header-title')]/span").text
            print(courseName)
            print(courseURL)
            print("--------")
            
        except Exception as e:
            print(f"Error retrieving course URL: {e}")
    
    time.sleep(10)

       

options = webdriver.ChromeOptions()
#options.add_argument("--headless=new")
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options = options, service = Service(ChromeDriverManager().install()))
driver.get("https://popcs.instructure.com/")
email = ""
password = ""
getCourses(email, password)

driver.quit()




    