import logging
from datetime import datetime


logging.basicConfig(
    filename="time.log",  
    level=logging.INFO,  
    format="%(asctime)s - %(levelname)s - %(message)s" ,
    datefmt="%Y-%m-%d"
)

current_date = datetime.now().strftime("%Y-%m-%d")

logging.info(current_date)

print("Лог записано у файл time.log")
