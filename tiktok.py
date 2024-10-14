import requests
from config import TT_key, TT_host

def download_tiktok_video(video_url, save_path='tiktok_video.mp4'):
    api_url = "https://tiktok-video-no-watermark2.p.rapidapi.com/"
    querystring = {"url": video_url, "hd": "1"}

    headers = {
        "x-rapidapi-key": f"{TT_key}",
        "x-rapidapi-host": f"{TT_host}"
    }

    response = requests.get(api_url, headers=headers, params=querystring)
    
    if response.status_code == 200:
        data = response.json()
        if data['code'] == 0:
            video_url = data['data']['play']  # URL для скачивания видео
            video_response = requests.get(video_url, stream=True)
            if video_response.status_code == 200:
                with open(save_path, 'wb') as video_file:
                    for chunk in video_response.iter_content(chunk_size=8192):
                        video_file.write(chunk)
                print(f"Видео успешно загружено: {save_path}")
            else:
                print("Ошибка при скачивании видео.")
        else:
            print(f"Ошибка API: {data['msg']}")
    else:
        print(f"Ошибка запроса: {response.status_code}")
    print(save_path)
    return save_path


# Пример использования
# video_url = "https://vm.tiktok.com/ZMhUDL2WR/"
# save_path = "YT_video.mp4"  # Путь для сохранения видео
# download_tiktok_video(video_url, save_path)
