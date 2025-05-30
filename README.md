# Telegram Media Downloader

A console script to download media from a Telegram chat, channel, or group.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Features

- Download media from Telegram chats, channels, and groups.
- Support for various media types: photos, videos, and more soon.
- Support download self-destructing media.
- Support download view-only media.
- Easy-to-use console interface.
- Customizable download settings.

## Installation

### Prerequisites

- Python 3
- [Telethon](https://github.com/LonamiWebs/Telethon) library

### Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/myounis1996/Telegram-Downloader.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Telegram-Downloader
    ```
3. Install Telethon:
    ```bash
    pip3 install telethon
    ```
   
## Configuration

This script requires the following environment variables:

- `api_id`: Your Telegram API id.
- `api_hash`: Your Telegram API hash.

### How to obtain `api_id` and `api_hash`

1. Go to [https://my.telegram.org/auth?to=apps](https://my.telegram.org/auth?to=apps) and log in with your Telegram account.
2. Click on **API development tools**.
3. Fill in the required fields (you can use any app title and short name).
4. After submitting, you will see your `api_id` and `api_hash` on the page.

Create a `config.py` file and add the following:

```env
api_id = your_telegram_api_id_here
api_hash = your_telegram_api_hash_here
```

## Usage

1. Configure the script with your Telegram API credentials.
2. Run the script:
    ```bash
    python main.py
    ```
   
## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.


## Acknowledgements

- [Telethon](https://github.com/LonamiWebs/Telethon) - A Python Telegram client library used to interact with the Telegram API.
- [Telegram API](https://core.telegram.org/api) - The API that enables interaction with Telegram's platform.
