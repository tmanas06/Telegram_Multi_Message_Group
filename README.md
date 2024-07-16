# Telegram Group Message Sender

This project is for sends messages of any lenth and size from a Google Sheets document to multiple Telegram groups using the Telethon library.

## Features

- Connects to Telegram using Telethon.
- Reads messages from a Google Sheet.
- there's no set limit to message length 
- Sends messages to specified Telegram groups.
- Handles errors such as flood errors and authorization issues.

## Requirements

- Python 3.6+
- Telegram API credentials
- Google Sheets API credentials

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/telegram-group-message-sender.git
    cd telegram-group-message-sender
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up your Telegram API credentials:
    - Create a `config.data` file in the root directory with the following content:
      ```ini
      [cred]
      id = YOUR_API_ID
      hash = YOUR_API_HASH
      phone = YOUR_PHONE_NUMBER
      ```

5. Set up Google Sheets API credentials:
    - Follow the [Google Sheets API setup guide](https://gspread.readthedocs.io/en/latest/oauth2.html#for-end-users-using-oauth-client-id) to create a `credentials.json` file.
    - Replace the `credentials.json` path in the script with the correct path to your file.

## Usage

1. Run the script:
    ```bash
    python bot.py
    ```

2. Follow the on-screen instructions to:
    - Authorize the Telegram client.
    - Select the groups to send messages to.
    - Ensure the messages are read from the Google Sheet and sent to the selected groups.

### Example Google Sheet

Ensure your Google Sheet is structured with messages in the first column. For example:

| Message |
|---------|
| Hello, group! |
| This is a test message. |


### Acknowledgements

- [Telethon](https://github.com/LonamiWebs/Telethon)
- [gspread](https://github.com/burnash/gspread)
- [oauth2client](https://github.com/google/oauth2client)

---
## Example of Application usage
 ```bash
    python Message.py
 ```
![image](https://github.com/user-attachments/assets/98e74f44-9f8e-49c0-a648-430e6be9685d)
![image](https://github.com/user-attachments/assets/d164fba1-32be-48c0-b19e-a517ce6bd149)


### Disclaimer

Use this script responsibly and ensure you comply with Telegram's terms of service and anti-spam policies.
If not you may end up getting banned...
