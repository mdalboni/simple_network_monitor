class BaseMonitor:

    def __init__(self, log_path):
        if not log_path:
            raise Exception('Log not found!')
        self.log_path = log_path

    def thread(self, *args, **kwargs):
        raise Exception('Not implemented')

    def log(self, message):
        from monitors import get_actual_time
        with open(self.log_path, 'a') as file:
            file.write(f'[{get_actual_time()}] {message}\n')
