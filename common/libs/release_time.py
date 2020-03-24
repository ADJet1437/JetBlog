from datetime import datetime

def get_release_time(format_str='%Y%m%d%H%M%S%f'):
    now = datetime.now()
    version = datetime.strftime(now, format_str)
    return version