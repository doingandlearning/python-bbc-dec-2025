class Headline:
    def __init__(self, text, source):
        self.text = text
        self.source = source
      
    def __str__(self):
      return f"{self.text} ({self.source})"

    def get_word_count(self):
      return len(self.text.split())


h = Headline(
    "General election: Labour and Tories clash over tax",
    "BBC News"
)

print(f"{h} is {h.get_word_count()} words long.")