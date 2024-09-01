# INST-BRUTE
This Python script performs a brute-force attack on the Instagram login page to attempt to guess the correct password for a given username. It utilizes a combination of Selenium and requests to mimic human behavior and make the brute-force attempts less detectable


## Features

#### Dynamic Headers and User Agents

```http
  Headers:
    User-Agent: (Randomly chosen from a list)
    X-Requested-With: XMLHttpRequest
    Referer: https://www.instagram.com/accounts/login/
    Origin: https://www.instagram.com
```

| Parameter     | Type     | Description                                                        |
| :------------ | :------- | :----------------------------------------------------------------- |
| `User-Agent`  | `string` | **Required**. Rotates through a list of user agents to simulate requests from different browsers. |
| `Referer`     | `string` | **Required**. The referrer URL to mimic legitimate traffic.          |
| `Origin`      | `string` | **Required**. The origin of the request to match Instagram’s expected headers. |

#### Proxy Rotation

```http
  Proxy:
    http://proxy_ip:proxy_port
```

| Parameter | Type     | Description                                                        |
| :-------- | :------- | :----------------------------------------------------------------- |
| `Proxy`   | `string` | **Required**. Rotates through a list of proxies to avoid IP blocking and maintain anonymity. |

#### Headless Browser Simulation

```http
  Browser: Chrome (Headless Mode)
```

| Parameter        | Type     | Description                                                        |
| :--------------- | :------- | :----------------------------------------------------------------- |
| `Browser`        | `string` | **Required**. Uses Selenium with a headless Chrome browser to interact with the login page. |
| `Headless Mode`  | `boolean` | **Required**. Runs the browser in headless mode to avoid GUI.       |

#### CSRF Token Extraction

```http
  GET /accounts/login/
```

| Parameter       | Type     | Description                                                        |
| :-------------- | :------- | :----------------------------------------------------------------- |
| `CSRF Token`    | `string` | **Required**. Extracts the CSRF token required for form submissions. |

#### Password File Handling

```http
  POST /accounts/login/ajax/
```

| Parameter         | Type     | Description                                                        |
| :---------------- | :------- | :----------------------------------------------------------------- |
| `Password File`   | `file`   | **Required**. Reads passwords from a file and attempts each one in sequence. |
| `Response Body`   | `HTML`   | **Optional**. Saves the response from Instagram into an HTML file if login is successful. |

#### Verbose Output

```http
  Verbose Mode:
    Prints detailed information about each login attempt.
```

| Parameter       | Type     | Description                                                        |
| :-------------- | :------- | :----------------------------------------------------------------- |
| `Verbose Mode`  | `boolean` | **Optional**. Enables printing of detailed information, including the password attempted, status codes, and response lengths. |

#### Error Handling

```python
  try:
      # Attempt login
  except Exception as e:
      print(f"Error: {e}")
```

| Parameter        | Type     | Description                                                        |
| :--------------- | :------- | :----------------------------------------------------------------- |
| `Error Handling` | `code`   | **Required**. Includes handling for request failures and exceptions to ensure the script continues running. |

---
# Important Note ⚠️
Brute-forcing login credentials is against Instagram’s terms of service and can be illegal. Use this script responsibly and only in authorized scenarios, such as for educational purposes or on your own accounts.

## requirements

To install the dependencies listed in requirements.txt, you can use the following command:

```bash
pip install -r requirements.txt
```
    

## Usage

```javascript
python3 insta_BF_unD.py
```
## تنبيه

آمل أن تستخدم هذا السكربت بشكل مسؤول وأخلاقي. تذكر دائمًا التصرف بنزاهة واحترام خصوصية وأمن الآخرين. تأكد من أن أفعالك تتماشى مع الإرشادات القانونية والأخلاقية. تذكر أن تحافظ على القيم مثل المسؤولية والاحترام لله في جميع مساعيك.3>
