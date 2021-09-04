import requests

TOKEN = "1991733241:AAHqEYNCXFZ85FS5x1TMiStPVqWJtyvbJjU"
url_photo = "https://api.telegram.org/bot{}/sendPhoto".format(TOKEN)
url_doc = "https://api.telegram.org/bot{}/sendDocument".format(TOKEN)
url_sticker = "https://api.telegram.org/bot{}/sendSticker".format(TOKEN)
url_message= "https://api.telegram.org/bot{}/sendMessage".format(TOKEN)
url_location = "https://api.telegram.org/bot{}/sendLocation".format(TOKEN)

def send_images(file_id,chat_id):#to send images
    data = {"chat_id": chat_id,"caption":'',"photo":file_id}
    response = requests.post(url_photo, data=data)
    print(f"You have a response of {response}")
send_images("file_id of image","your chat_id")

def send_images_url(image_url,chat_id):#to send images with https url
    data = {"chat_id": chat_id,"caption":'',"photo":image_url}
    response = requests.post(url_photo, data=data)
    print(f"You have a response of {response}")
send_images_url("https url of image","your chat_id")

def send_doc(doc_link,chat_id):#to send documents
    data = {"chat_id": chat_id,"document":doc_link}
    response = requests.post(url_doc, data=data)
    print(f"You have a response of {response}")
send_doc("file_id of file","your chat_id")

def send_doc_url(doc_link,chat_id):#to send documents with url
    data = {"chat_id": chat_id,"document":doc_link}
    response = requests.post(url_doc, data=data)
    print(f"You have a response of {response}")
send_doc("https url of doc","your chat_id")

def send_sticker(file_id,chat_id):#to send sticker
    data = {"chat_id": chat_id,"sticker":file_id}
    response = requests.post(url_sticker, data=data)
    print(f"You have a response of {response}")
send_sticker("file_id of sticker","your chat_id")

def send_message(text,chat_id):#to send text message
    data = {"chat_id": chat_id,"text":text}
    response = requests.post(url_message, data=data)
    print(f"You have a response of {response}")
send_message("text to send","your chat_id")

def send_location(latitude,longitude,chat_id):#to send your location
    data = {"chat_id": chat_id,"latitude":latitude,"longitude":longitude}
    response = requests.post(url_location, data=data)
    print(f"You have a response of {response}")
send_location("your lattiude","your longitude","your chat_id")