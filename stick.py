import requests

def send_photo(token, chat_id, photo_path):
    url = f"https://api.telegram.org/bot{token}/sendPhoto"
    files = {'photo': open(photo_path, 'rb')}
    data = {'chat_id': chat_id}
    response = requests.post(url, files=files, data=data)
    if response.status_code == 200:
        print("Фото успішно відправлено!")
    else:
        print("Виникла помилка при відправці фото:", response.status_code)

if __name__ == "__main__":
    # Ваш токен доступу
    token = '5489176408:AAF17syyg5625iXqJwN1NrYW2wnXFTjNxX8'

    # ID чату або ідентифікатор користувача, куди ви хочете відправити фото
    chat_id = '6102707950'  # Замініть на ID вашого чату або користувача

    # Шлях до фотографії, яку ви хочете відправити
    photo_path = 'sticker.webp'

    send_photo(token, chat_id, photo_path)
