from abc import ABC, abstractmethod

from matplotlib import pyplot


class BaseChart(ABC):
    @abstractmethod
    def get_data(self):
        ...

    @abstractmethod
    def create_chart(self):
        ...

    @staticmethod
    def gather_and_show(charts: ['BaseChart']):
        for chart in charts:
            chart.get_data()
            chart.create_chart()
        pyplot.show()
