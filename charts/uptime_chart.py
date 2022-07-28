from matplotlib import pyplot

from charts.base_chart import BaseChart


class UptimeChart(BaseChart):

    def __init__(self):
        super().__init__()
        self.csv = 'uptime_monitor.csv'
        self.elapsed_time_list = []
        self.time_list = []

    def get_data(self):
        with open(self.csv, 'r') as file:
            for line in file.readlines():
                elapsed_time, time = line.split(',')
                self.elapsed_time_list.append(int(elapsed_time))
                self.time_list.append(time)

    def create_chart(self):
        pyplot.xlabel('Time')
        pyplot.ylabel('Elapsed time')
        pyplot.plot(self.time_list, self.elapsed_time_list, label='Response')
        pyplot.savefig('uptime_chart.jpg')
        pyplot.close()
