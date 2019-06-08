import time
import os
import datetime


class Clock(object):
    def __init__(self, cur_time):
        time_list = cur_time.split(':')
        self._hour = int(time_list[0])
        self._minute = int(time_list[1])
        self._second = int(time_list[2])

    def run(self):
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        return '%02d:%02d:%02d' % (self._hour, self._minute, self._second)


clock = Clock(datetime.datetime.now().strftime('%H:%M:%S'))
while True:
    os.system('clear')
    print(clock.show())
    time.sleep(1)
    clock.run()
