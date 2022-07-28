from threading import Thread
from time import sleep

import speedtest

from monitors.base_monitor import BaseMonitor
from monitors.utils import get_actual_time


class SpeedTestMonitor(BaseMonitor):

    def __init__(self):
        super().__init__(log_path='speed.log')
        self.speed_test = speedtest.Speedtest()

    @staticmethod
    def bytes_to_mb(bytes) -> int:
        if bytes > 0:
            KB = 1024  # One Kilobyte is 1024 bytes
            MB = KB ** 2  # One MB is 1024 KB
            return int(bytes / MB)
        return 0

    @staticmethod
    def thread(*args, **kwargs):
        print(
            f'[{get_actual_time()}] Speed Thread starting...'
        )
        Thread(
            target=SpeedTestMonitor().monitor,
            args=args,
            daemon=True
        ).start()
        print(
            f'[{get_actual_time()}] Speed Thread started...'
        )

    def monitor(self, seconds=10, file_path='speed_monitor.csv'):
        self.log('Thread running...')
        execution = 0
        while True:
            download = self.bytes_to_mb(self.download_monitor())
            upload = self.bytes_to_mb(self.upload_monitor())
            with open(file_path, 'a') as file:
                file.write(f'{download},{upload},{get_actual_time()}\n')
            self.log(
                f'Execution #{execution} data '
                f'download: {download} upload: {upload}'
            )
            sleep(seconds)
            execution += 1

    def download_monitor(self) -> int:
        try:
            return self.speed_test.download()
        except:
            return 0

    def upload_monitor(self) -> int:
        try:
            return self.speed_test.upload()
        except:
            return 0
