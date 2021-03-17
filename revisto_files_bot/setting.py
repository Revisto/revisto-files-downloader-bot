import dotenv
from os import getenv

dotenv.load_dotenv()

save_location = "/root/shared_data/"
telegram_access_token = getenv("telegram_robot_access_token")