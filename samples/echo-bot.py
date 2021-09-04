# ! can only work with emoji's and text's not files and photos
# 1991733241:AAHqEYNCXFZ85FS5x1TMiStPVqWJtyvbJjU -->user created bot's token
import json 
import requests
TOKEN = "1991733241:AAHqEYNCXFZ85FS5x1TMiStPVqWJtyvbJjU"
URL = f"https://api.telegram.org/bot{TOKEN}/"
url_message= "https://api.telegram.org/bot{}/sendMessage".format(TOKEN)
current_url = ""
updateid_list =[]
next_updateid = None
def send_message(text,chat_id):
    data = {"chat_id": chat_id,"text":text}
    response = requests.post(url_message, data=data)
    print(f"Successfully send message wuth response {response}")

def reception(updateid):
    if updateid == None:
        current_url = URL + f"getUpdates?timeout=100&offset=None"
    else:
        current_url = URL + f"getUpdates?timeout=100&offset={updateid}"
    response = requests.get(current_url)
    content = response.content.decode("utf8")
    js = json.loads(content)
    num_updates = len(js["result"])
    if num_updates>0:
        last_update = num_updates - 1
        chat_id = js["result"][last_update]["message"]["chat"]["id"]
        updateid_list.append(js["result"][last_update]['update_id'])
        if 'text' in js["result"][last_update]["message"]:
            text = js["result"][last_update]["message"]["text"]
            print(f"I received a message {text} from {chat_id}")
            send_message(text,chat_id)
        else:
            send_message("Please send a text format message",chat_id)
while True:
    reception(next_updateid)
    next_updateid = max(updateid_list)+1
