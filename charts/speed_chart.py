from matplotlib import pyplot

from charts.base_chart import BaseChart


class SpeedChart(BaseChart):

    def __init__(self):
        super().__init__()
        self.csv = 'speed_monitor.csv'
        self.download_list = []
        self.upload_list = []
        self.time_list = []

    def get_data(self):
        with open(self.csv, 'r') as file:
            for line in file.readlines():
                download, upload, time = line.split(',')
                self.download_list.append(int(download))
                self.upload_list.append(int(upload))
                self.time_list.append(time)

    def create_chart(self):
        pyplot.xlabel('Time')
        pyplot.ylabel('Megabytes')
        pyplot.plot(self.time_list, self.download_list, label='Download')
        pyplot.plot(self.time_list, self.upload_list, label='Upload')
        pyplot.legend()
        pyplot.savefig('speed_chart.jpg')
        pyplot.close()
