from threading import Thread
from time import sleep

from requests import get

from monitors.base_monitor import BaseMonitor
from monitors.utils import get_actual_time


class ConnectionUptimeMonitor(BaseMonitor):
    def __init__(self, url='https://google.com', time=30):
        super().__init__(log_path='uptime.log')
        self.url = url
        self.time = time

    @staticmethod
    def thread(*args, **kwargs):
        print(
            f'[{get_actual_time()}] Uptime Thread starting...'
        )
        Thread(
            target=ConnectionUptimeMonitor().monitor,
            args=args,
            daemon=True
        ).start()
        print(
            f'[{get_actual_time()}] Uptime Thread started...'
        )

    def monitor(self, seconds=10, file_path='uptime_monitor.csv'):
        self.log('Thread running...')
        execution = 0
        while True:
            time_elapsed = self.fetch_page()
            with open(file_path, 'a') as file:
                file.write(f'{time_elapsed},{get_actual_time()}\n')
            self.log(
                f'Execution #{execution} data elapsed_time: {time_elapsed}'
            )
            sleep(seconds)
            execution += 1

    def fetch_page(self) -> int:
        try:
            response = get(self.url, timeout=60)
            return int(response.elapsed.total_seconds())
        except:
            return -1
