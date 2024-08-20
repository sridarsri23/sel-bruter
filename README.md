Sel-Bruter - Login bruteforceing Using Selenium and Tor

⚠️ Important Notice: Any malicious use of this tool is strictly prohibited. This script is intended solely for ethical and educational practices. Unauthorized access to systems or networks without explicit permission is illegal and unethical.
Features

    Resume Capability: The script saves the last attempted username and password, allowing it to resume from where it left off.
    Tor Integration: Traffic is routed through the Tor network, ensuring anonymity.
    Customizable: You can specify your own username, password list, and target URL.

Requirements

    Python 3.x: Ensure that Python is installed on your system.
    Selenium: Python package for browser automation.
    GeckoDriver: Driver for Firefox, used by Selenium.
    Firefox ESR: Extended Support Release of Firefox, configured to work with Tor.
    Tor: Installed and running on your machine.

Python Packages

You can install the necessary Python packages using pip:

bash

pip install selenium

Additional Tools

    GeckoDriver: Download and place it in /usr/local/bin/ or your preferred directory.
    Firefox ESR: Ensure it's installed and accessible at /usr/bin/firefox-esr.
    Tor: Make sure Tor is running on your machine, with the default SOCKS5 proxy available at 127.0.0.1:9050.

Setup

    Clone the Repository:

    bash

git clone https://github.com/yourusername/your-repo.git
cd your-repo

Edit the Script:

    Modify the gecko_driver_path and firefox_path variables if your paths differ.
    Update the login_url to point to the target login page.
    Replace the usernames and password file path /home/blackbike/PT/combined_wordlist_temp.txt with your own.

Prepare the Environment:

    Ensure Tor is running: sudo service tor start
    Verify that the Tor SOCKS5 proxy is correctly configured to run on 127.0.0.1:9050.

Running the Script:

Execute the script with Python:

bash

    python3 Sel-Bruter.py

How It Works

    The script reads usernames and passwords from specified lists.
    It attempts to log in to the given URL using these credentials.
    If a login attempt is successful (detected by a change in URL), it prints the successful credentials.
    The script saves the last attempted username and password to last_attempt.txt, enabling the resumption of the script from the last failure if interrupted.

Logs

    The script logs its progress and any errors encountered during execution. The Geckodriver logs are stored in /home/blackbike/PT/geckodriver.log.

Troubleshooting

    Tor Configuration: If the script is not routing traffic through Tor, verify that Tor is running and the SOCKS5 proxy settings are correct.
    Firefox Path: Ensure that the path to Firefox ESR is correct. Adjust the firefox_path variable if necessary.
    GeckoDriver Path: Make sure the GeckoDriver executable is in the correct location and that the path is specified correctly in the script.

Disclaimer

This script is for educational purposes only. Unauthorized use of this script to access systems without permission is illegal. Always ensure you have explicit authorization before attempting to access any system.
Contributions

Contributions are welcome! Feel free to submit a pull request or open an issue.
License

This project is licensed under the MIT License - see the LICENSE file for details.
