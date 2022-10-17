from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("5406248685:AAG5m_W1jdIihdPGd4WfPXaZHeDxdZvIxJQ")  # Bot toekn
ADMINS = env.list("1871081893")  # adminlar ro'yxati
IP = env.str("ip")  # Xosting ip manzili
