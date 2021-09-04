#This is bot powered file storage system
# 1991733241:AAHqEYNCXFZ85FS5x1TMiStPVqWJtyvbJjU -->user created bot's token
import json 
import requests
TOKEN = "1991733241:AAHqEYNCXFZ85FS5x1TMiStPVqWJtyvbJjU"
URL = f"https://api.telegram.org/bot{TOKEN}/"
url_doc = "https://api.telegram.org/bot{}/sendDocument".format(TOKEN)
url_message= "https://api.telegram.org/bot{}/sendMessage".format(TOKEN)
current_url = ""
updateid_list =[]
current_sub = " "
next_updateid = None
sub_dic = {}

def send_doc(doc_links,chat_id):
    for doc_link in doc_links:
        data = {"chat_id": chat_id,"document":doc_link}
        response = requests.post(url_doc, data=data)
        print(f"You have a response of {response}")
def send_message(text,chat_id):
    data = {"chat_id": chat_id,"text":text}
    response = requests.post(url_message, data=data)
    print(f"Successfully send message wuth response {response}")

def reception(updateid,current_sub):
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
            if text in sub_dic:
                send_doc(sub_dic[text],chat_id)
            else:
                print(f"I received a message {text} from {chat_id}")
                current_sub = text
                sub_dic[current_sub] =[]
                send_message(f"Sure please upload files for {text}",chat_id)
        elif 'document' in js["result"][last_update]["message"]:
            file_id = js["result"][last_update]["message"]['document']['file_id']
            if current_sub == " ":
                send_message("Please add a subject",chat_id)
            else:
                sub_dic[current_sub].append(file_id)
                print("I received a file from {chat_id}")
        return(next_updateid,current_sub)

            
while True:
    next_updateid,current_sub=reception(next_updateid,current_sub)
    next_updateid = max(updateid_list)+1
