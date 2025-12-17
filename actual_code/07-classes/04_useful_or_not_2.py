slot = {
    "programme": "News at Six",
    "start": 18,
    "end": 19
}

def duration(slot):
    return slot["end"] - slot["start"]

print(duration(slot))
print(slot["end"] - slot["start"])


class ScheduleSlot:
    def __init__(self, programme, start, end):  # object initialiser or constructor
        if end <= start:
            raise ValueError("End must be after start")
        self.programme = programme
        self.start = start
        self.end = end

    def duration(self):
        return self.end - self.start

    def is_news(self):
        return "news" in self.programme.lower()

    def __str__(self):
      return f"{self.programme} starts at {self.start} and ends at {self.end} lasting {self.duration()}"

slot2 = ScheduleSlot("Traitors", 21, 22)
print(slot2.duration())
print(slot2)