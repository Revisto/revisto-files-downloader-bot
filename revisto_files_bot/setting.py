import dotenv
from os import getenv

dotenv.load_dotenv()

base_save_location = "/root/shared_data/telegram/"
music_save_location = f"{base_save_location}musics/"
video_save_location = f"{base_save_location}videos/"
picture_save_location = f"{base_save_location}pictures/"
telegram_access_token = getenv("telegram_robot_access_token")