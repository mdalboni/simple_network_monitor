from charts.base_chart import BaseChart
from charts.speed_chart import SpeedChart
from charts.uptime_chart import UptimeChart


def show_graphs():
    BaseChart.gather_and_show([SpeedChart(), UptimeChart()])
