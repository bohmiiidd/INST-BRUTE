# INST-BRUTE
This Python script performs a brute-force attack on the Instagram login page to attempt to guess the correct password for a given username. It utilizes a combination of Selenium and requests to mimic human behavior and make the brute-force attempts less detectable

Features:

    Dynamic Headers and User Agents:
        The script rotates through a list of user agents to simulate requests from different browsers, making the attacks appear more like genuine user interactions.

    Proxy Rotation:
        To further obscure the attack and avoid IP blocking, the script rotates through a list of proxies. Each request can be sent through a different proxy, which helps in maintaining anonymity and bypassing rate limits.

    Headless Browser Simulation:
        Uses Selenium with a headless Chrome browser to interact with the Instagram login page. This approach mimics real user behavior, such as delays between actions, and captures necessary cookies for authentication.

    CSRF Token Extraction:
        Extracts the CSRF token required for form submissions from the initial login page request, ensuring that the login attempts are valid and accepted by Instagram.

    Password File Handling:
        Reads passwords from a file and tries each one in sequence. If a password is found, the script saves the response from Instagram into an HTML file for review.

    Verbose Output:
        When enabled, prints detailed information about each login attempt, including the password being tried, status codes, and response lengths. This feature aids in monitoring the progress of the brute-force attack.

    Error Handling:
        Includes error handling for request failures and exceptions to ensure the script continues running even if individual requests fail.

Important Note: Brute-forcing login credentials is against Instagram’s terms of service and can be illegal. Use this script responsibly and only in authorized scenarios, such as for educational purposes or on your own accounts.

## requirements

 To install the dependencies listed in requirements.txt, you can use the following command:

```bash
pip install -r requirements.txt
```
    

## Usage

```javascript
python3 insta_BF_unD.py
```

