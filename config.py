import os
import logging
from logging.handlers import RotatingFileHandler




BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
API_ID = int(os.environ.get("API_ID", ""))
API_HASH = os.environ.get("API_HASH", "")


OWNER_ID = int(os.environ.get("OWNER_ID", ""))
DB_URL = os.environ.get("DB_URL", "")
DB_NAME = os.environ.get("DB_NAME", "madflixbotz")


CHANNEL_ID = int(os.environ.get("CHANNEL_ID", ""))
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "0"))


# FILE_AUTO_DELETE = int(os.getenv("FILE_AUTO_DELETE", "600")) # auto delete in seconds


PORT = os.environ.get("PORT", "8080")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))



try:
    ADMINS=[6848088376]
    for x in (os.environ.get("ADMINS", "6848088376").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")









CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

DISABLE_CHANNEL_BUTTON = True if os.environ.get('DISABLE_CHANNEL_BUTTON', "True") == "True" else False

BOT_STATS_TEXT = "<b>BOT UPTIME :</b>\n{uptime}"







USER_REPLY_TEXT = "⚠️Peringatan⚠️\n\nJangan Mengirimkan Pesan Kepada Bot Karna Bot ini tidak akan merespon anda, Jika Anda pertanyaan silahkan pc admin\n @estelerkuu"

START_MSG = os.environ.get("START_MESSAGE", "Hello {first}\n\nSaya dapat menyimpan file dan user dapat mengaksesnya dari link khusus, Join VIP \n@estelerkuu")

FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>Halo {first}\nSilahkan Baca Dulu Cara Penggunaan Bot Ini\n\n[ TUTOR BOT ]\nSilahkan Pencet Tombol Join Yang diminta Oleh BOT pada bagian bawah Terlebih Dahulu. Jika Kamu Sudah Join Pencet Tombol Coba Lagi lalu start.\n\nJika tidak ingin ribet JOIN VIP, cek harganya di bawah :\nVIP LIST INDOVIRAL :\n✣ VIP LOKAL NUSANTARA ┈➤ Rp. 40.000\n✣ VIP ONLYFANS ┈➤ Rp. 25.000\n✣ VIP BOCIL PREMIUM ┈➤ Rp. 50.000\n✣ VIP BOCIL SUPER PREMIUM ┈➤ Rp. 100.000\n✣ VIP HIJAB ┈➤ Rp. 35.000\n✣ TAKE ALL VIP ( JOIN SEMUA VIP BONUS VIP JAV ) ┈➤ Rp. 150.000\nBebas nonton tanpa ribet menggunakan Link/Iklan, Sekali bayar PERMANENT.\nLangsung akses ribuan video terbaru dan terupdate, Video akan diperbaharui setiap harinya\nMinat? Hubungi admin\n@estelerkuu</b>")





ADMINS.append(OWNER_ID)
ADMINS.append(6848088376)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   





# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
