from datetime import datetime


def get_actual_time() -> str:
    return str(datetime.now()).split('.')[0]
