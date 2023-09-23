Binance P2P Rate Notifier
=========================

Table of Contents
-----------------

-   [Overview](https://chat.openai.com/c/2fa3fe9a-ddf5-4086-877d-4f37c782df9c#overview)
-   [Getting Started](https://chat.openai.com/c/2fa3fe9a-ddf5-4086-877d-4f37c782df9c#getting-started)
    -   [Prerequisites](https://chat.openai.com/c/2fa3fe9a-ddf5-4086-877d-4f37c782df9c#prerequisites)
    -   [Installation](https://chat.openai.com/c/2fa3fe9a-ddf5-4086-877d-4f37c782df9c#installation)
-   [Usage](https://chat.openai.com/c/2fa3fe9a-ddf5-4086-877d-4f37c782df9c#usage)
-   [Contributing](https://chat.openai.com/c/2fa3fe9a-ddf5-4086-877d-4f37c782df9c#contributing)
-   [License](https://chat.openai.com/c/2fa3fe9a-ddf5-4086-877d-4f37c782df9c#license)

Overview
--------

The Binance P2P Rate Notifier is a Python script that automates the process of fetching the Binance P2P exchange rate for Naira (BTC to NGN) and sending a notification via Twilio SMS. It uses the Selenium web scraping library to retrieve the exchange rate from the Binance website and the Twilio API to send SMS notifications.

Getting Started
---------------

### Prerequisites

Before running the script, you'll need to have the following:

1.  Python 3 installed on your system.

2.  Chrome web browser installed.

3.  ChromeDriver installed and its path set correctly in the script (`chrome_driver_path`).

4.  Binance API key and secret for web scraping.

5.  Twilio Account SID and Auth Token for sending SMS notifications.

### Installation

1.  Clone this repository to your local machine:

    bashCopy code

    `git clone https://github.com/yourusername/binance-p2p-rate-notifier.git`

2.  Navigate to the project directory:

    bashCopy code

    `cd binance-p2p-rate-notifier`

3.  Create a virtual environment (optional but recommended):

    bashCopy code

    `python -m venv venv`

4.  Activate the virtual environment:

    -   On Windows:

        bashCopy code

        `venv\Scripts\activate`

    -   On macOS and Linux:

        bashCopy code

        `source venv/bin/activate`

5.  Install the required Python packages:

    bashCopy code

    `pip install -r requirements.txt`

Usage
-----

1.  Set up the necessary environment variables by creating a `.env` file in the project directory with the following content:

    plaintextCopy code

    `ACCOUNT_SID=your_twilio_account_sid
    AUTH_TOKEN=your_twilio_auth_token`

2.  Edit the `chrome_driver_path` variable in the Python script to point to your ChromeDriver executable.

3.  Run the script to fetch the Binance P2P exchange rate and send an SMS notification:

    bashCopy code

    `python binance_p2p_notifier.py`

    The script will launch a Chrome browser, navigate to the Binance P2P page, fetch the exchange rate, send an SMS notification, and then quit the browser.

Contributing
------------

If you would like to contribute to this project, please open an issue or submit a pull request. We welcome contributions from the community!

License
-------

This project is licensed under the MIT License - see the [LICENSE](https://chat.openai.com/c/LICENSE) file for details.