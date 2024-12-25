import time
import datetime

class Timer():
    def __init__(self):
        self._timer_star_time = None
        self._elapsed_time = 0

    def start_timer(self):
        if self._timer_star_time is None:
            self._timer_star_time = time.time()
        else:
            print("Счетчик уже запущен.")
        
    def stop_timer(self):
        if self._timer_star_time is not None:
            self._elapsed_time += time.time() - self._timer_star_time
            self._timer_star_time = None
        else:
            print("Счетчик не запущен.")

    def get_elapsed_time(self):
        if self._timer_star_time is not None:
            return self._elapsed_time + (time.time() - self._timer_star_time)
        return self._elapsed_time