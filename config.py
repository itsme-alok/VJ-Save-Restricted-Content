import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "29202984"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "a8f99f222194e1db2d93917ef21a3951")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://014alokprakashdubey:t4uCFDw8d8vz2dTq@cluster0.tulj3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
