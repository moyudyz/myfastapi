import os
import time
from loguru import logger

basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


log_path = os.path.join(basedir, 'logs')

if not os.path.exists(log_path):
    os.mkdir(log_path)


log_path_error = os.path.join(
    log_path, f'{time.strftime("%Y-%m-%d")}_error.log')

logger.add(log_path_error, rotation="12:00", retention="5 days", enqueue=True)
