headlines = [
    "General election: Labour and Tories clash over tax",
    "England crowned T20 world champions",
    "Summer travel chaos feared as airline strikes loom",
    "UK inflation rate falls to lowest level in three years",
    "New David Hockney exhibition opens in London",
    "Science discovers new way to tackle plastic waste",
    "Government announces new funding for NHS",
    "Stock market hits record high on tech boom",
    "Debate rages over future of Artificial Intelligence",
    "Classic Doctor Who episodes to be released in colour"
]

headline_lengths = []
for headline in headlines:
  headline_lengths.append(len(headline.split()))

print(headline_lengths)

headline_lengths_list_comp = [len(headline.split()) for headline in headlines]

short_headlines = []
for headline in headlines:
  if len(headline.split()) < 7:
    short_headlines.append(headline)

print(short_headlines)

short_headlines_list_comp = [headline for headline in headlines if len(headline.split()) < 7]
print(short_headlines_list_comp)

just_new_lengths = []
for headline in headlines:
  if "new" in headline.lower():
    just_new_lengths.append(len(headline.split()))

print(just_new_lengths)

just_new_lengths_list_comp = [len(headline.split()) 
                                  for headline in headlines 
                                  if "new" in headline.lower()
                              ]
print(just_new_lengths_list_comp)