from time import sleep

from monitors.speed_monitor import SpeedTestMonitor
from monitors.uptime_monitor import ConnectionUptimeMonitor
from monitors.utils import get_actual_time


def execute():
    SpeedTestMonitor.thread()
    ConnectionUptimeMonitor.thread()
    while True:
        sleep(60)
        print(
            f'[{get_actual_time()}] '
            'It is still working, you can check the logs in the root folder'
        )
