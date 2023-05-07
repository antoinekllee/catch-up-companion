# Catch-up Companion 🚀

Catch-up Companion is a WhatsApp bot designed to help you stay up-to-date with your group chat conversations. By summarizing the last n messages in a group chat, Catch-up Companion allows you to quickly catch up on missed conversations. The bot is built using Twilio, Flask, and the OpenAI GPT API. 🤖

![Catch-up Companion Logo](logo.png)

## Features 💬

- Add the bot to WhatsApp group chats 📱
- Summarize the last n messages in a chat
- Automatic summarization using the OpenAI GPT API 🚀

## Requirements 🛠️

- Python 3.6 or later
- Twilio account
- OpenAI GPT API key
- Flask

## Getting Started 🚀

1. **Clone the repository**

```bash
git clone https://github.com/antoinekllee/catch-up-companion.git
cd catch-up-companion
```

2. **Install the required packages**

```bash
pip install twilio flask openai
```

3. **Set up a Twilio account and connect it to WhatsApp**

- Sign up for a free Twilio account (https://www.twilio.com/try-twilio)
- From the Twilio Console, go to the "All Products & Services" menu and click on "Programmable SMS"
- Click "Try it Out" and then "Try WhatsApp"
- Follow the instructions to connect your WhatsApp account to your Twilio Sandbox environment

4. **Set up an OpenAI GPT API key**

- Sign up for an API key at OpenAI (https://beta.openai.com/signup/)
- Note down your API key for the next step

5. **Configure the bot**

- Create a `.env` file using the provided `.env.template` file
- Fill in the following information in the `.env` file:
  - `OPENAI_KEY` with your OpenAI GPT API key
  - `TWILIO_SID` with your Twilio Account SID
  - `TWILIO_TOKEN` with your Twilio Auth Token
  - `BOT_PHONE_NUMBER` with your Twilio Sandbox phone number

6. **Run the bot**

```bash
python app.py
```

7. **Expose your local app to the internet**

- Use a tool like ngrok (https://ngrok.com/) to expose your local app to the internet:

```bash
ngrok http 5000
```

- Copy the ngrok URL (e.g., `https://your-ngrok-url.ngrok.io/bot`) and configure it as the webhook for your Twilio WhatsApp Sandbox (in the Twilio Console)

8. **Test the bot**

- Add the bot to your WhatsApp group chat
- To get a summary of the last n messages, send "summarise n" to the group chat

## Usage 📝

- Add the bot to your WhatsApp group chat
- When you want to catch up on missed conversations, send a message in the format `summarise n` (e.g., `summarise 10`)
- The bot will summarize the last n messages in the group chat and send the summary back to the group

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
