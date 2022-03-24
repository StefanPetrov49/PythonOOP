class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def next_second(self):
        hours, minutes, seconds = self.get_time().split(':')
        hours, minutes, seconds = int(hours), int(minutes), int(seconds)+1
        if seconds > self.max_seconds:
            seconds = 0
            minutes += 1
        if minutes > self.max_minutes:
            minutes = 0
            hours += 1
        if hours > self.max_hours:
            hours = 0
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"



time = Time(9, 30, 59)
print(time.next_second())
time = Time(10, 59, 59)
print(time.next_second())
time = Time(23, 59, 59)
print(time.next_second())



