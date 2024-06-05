# PhishPhucker

![PhishPhucker Logo](https://i.ibb.co/jD9dqMm/openart-image-5-C4-YIl-FF-1717586639754-raw.jpg)

## Overview

Welcome to **PhishPhucker**, the revolutionary open-source cybersecurity tool designed to disrupt the phishing industry like never before. PhishPhucker ingests public and custom phishing feeds/URLs, scans them, and launches sophisticated countermeasures to thwart phishing attacks. Our mission is to make phishing an unprofitable and ineffective endeavor by mimicking real user behavior and overwhelming attackers with arbitrary but human-like data.

## Features

- **Ingest Multiple Phishing Feeds**: Seamlessly integrate public phishing feeds and custom URLs for comprehensive coverage.
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

- Python 3.11 or higher
- Docker (optional, for containerized deployment)
- Chrome Driver
- Git

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/PhishPhucker.git
   cd PhishPhucker
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   ```bash
   python phishphucker.py
   ```

4. **(Optional) Deploy with Docker**:
   ```bash
   docker build -t phishphucker .
   docker run -d phishphucker
   ```

## Usage

1. **Feed Ingestion**:
   - Add public phishing feeds or custom URLs to the `feeds.txt` file.
   - Run the ingestion module to fetch the latest data.
     ```bash
     python ingest_feeds.py
     ```

2. **Perform Website Scan**:
   - Execute the scan to extract phishing kits and endpoints.
     ```bash
     python web_scan.py
     ```

3. **Disrupt Phishing Operations**:
   - Launch the disruption module to send arbitrary data to attackers.
     ```bash
     python disrupt.py
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

