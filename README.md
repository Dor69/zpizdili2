# TikTok | Reels video downloader TG Bot

This is a Telegram bot that downloads media from TikTok and Instagram. 

## Getting Started

To start using the bot, follow these steps:

1. Clone the repository or download the files.
2. Navigate to the project directory.
3. Make sure you have Python installed on your machine.

## Installation

You need to install the required libraries. Run the following command in your terminal:

```bash
pip install -r requirements.txt
```

## Configuration

Before running the bot, you need to configure it:

1. Rename `config.py.dist` to `config.py`.
2. Open `config.py` and fill in the following fields:

```python
TG_token = ''          # Your Telegram Bot Token
Insta_key = ''        # Your Instagram API key
Insta2_host = ''      # Your Instagram API host
TT_key = ''           # Your TikTok API key
TT_host = ''          # Your TikTok API host
```

## APIs Used

- **TikTok API**: [Tiktok video no watermark](https://rapidapi.com/yi005/api/tiktok-video-no-watermark2).
- **Instagram API**: [Instagram Bulk Scraper API](https://rapidapi.com/mrngstar/api/instagram-bulk-scraper-latest).

## Running the Bot

To run the bot, execute the following command in your terminal:

```bash
python Spizdili_V2.py
```