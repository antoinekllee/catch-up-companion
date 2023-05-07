from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import openai

from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

# Replace with your OpenAI GPT API key
openai.api_key = os.getenv("OPENAI_KEY")

# Replace with your Twilio Account SID and Auth Token
account_sid = os.getenv("TWILIO_SID")
auth_token = os.getenv("TWILIO_TOKEN")

def get_last_n_messages(n, sender_phone_number):
    client = Client(account_sid, auth_token)
    all_messages = client.messages.list(
        to=os.getenv("BOT_PHONE_NUMBER"),
        from_=sender_phone_number
    )

    messages = sorted(all_messages, key=lambda msg: msg.date_sent, reverse=True)
    return messages[:n]

def summarize_messages(messages): 
    text = " ".join([msg.body for msg in messages])

    with open('prompt.txt', 'r') as f:
        prompt = f.read()

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": f"Message history: {text}"},
        ], 
        temperature=0.7,
        max_tokens=500
    )
    return response['choices'][0]['message']['content']

@app.route('/bot', methods=['POST'])
def bot():
    print("CALLED BOT ROUTE")

    incoming_message = request.values.get('Body', '').lower()
    sender_phone_number = request.values.get('From', '')
    response = MessagingResponse()
    message = response.message()

    if incoming_message.startswith('summarise'):
        try:
            n = int(incoming_message.split(' ')[1])
            messages = get_last_n_messages(n, sender_phone_number)
            summary = summarize_messages(messages)

            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print(type(messages))
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print(messages)
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print(type(summary))
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print(summary)
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

            message.body(summary)

        except ValueError:
            message.body('Invalid input. Please enter a number after "summarise".')
        except Exception as e:
            message.body(f'Error: {str(e)}')
    else:
        message.body('To get a summary of the last n messages, send "summarise n".')

    return str(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)