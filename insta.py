import requests
from config import Insta_key, Insta2_host

# Укажите URL с API для получения информации по короткому коду (shortcode)
def dowload_reels(shortcode):
    url = f"https://instagram-bulk-scraper-latest.p.rapidapi.com/media_info_from_shortcode/{shortcode}"
    # Укажите заголовки для авторизации
    headers = {
        "x-rapidapi-key": f"{Insta_key}",
        "x-rapidapi-host": f"{Insta2_host}"
    }
    # Получаем информацию о медиа по короткому коду
    response = requests.get(url, headers=headers)
    # Проверяем успешность запроса
    if response.status_code == 200:
        data = response.json()
        # Получаем URL видео
        video_url = data.get("data", {}).get("video_url")
        
        if video_url:
            # Задаем имя файла для сохранения видео
            video_file_name = "instagram_video.mp4"
            
            # Загружаем видео
            video_response = requests.get(video_url)
            
            # Проверяем успешность загрузки видео
            if video_response.status_code == 200:
                # Сохраняем видео в файл
                with open(video_file_name, 'wb') as f:
                    f.write(video_response.content)
                print(f"Видео успешно загружено и сохранено как {video_file_name}")
            else:
                print("Не удалось загрузить видео.")
        else:
            print("Не удалось найти URL видео в ответе.")
    else:
        print(f"Ошибка при выполнении запроса: {response.status_code}")
    return video_file_name
def format_instagram_url(url):
    # Разбиваем URL на части, чтобы выделить shortcode
    parts = url.split('/')
    
    # Ищем короткий код среди частей URL
    for part in parts:
        if len(part) == 11:  # Обычно shortcode имеет длину 11 символов
            shortcode = part
            break
    else:
        return "Invalid URL format or shortcode not found."
    
    # Формируем новый URL с использованием найденного shortcode
    formatted_url = f"https://www.instagram.com/reel/{shortcode}/?igsh=dG1wZjY5d3VzYzFv"
    return shortcode

# Пример использования
# a = format_instagram_url('https://www.instagram.com/reel/C_cDmv5xARL/')
# dowload_reels(a)