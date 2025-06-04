
import random
future_list= ["Don't pursue happiness – create it.",
"All things are difficult before they are easy.",
"The early bird gets the worm, but the second mouse gets the cheese.",
"Someone in your life needs a letter from you.",
"Don't just think. Act!",
"Your heart will skip a beat.",
"The fortune you search for is in another cookie.",
"Help! I'm being held prisoner in a Chinese bakery!"]
def fortune():
  future = random.choice(future_list)
  return future


print("\n✨ Your Fortune Cookie Says ✨")
print("=" * 30)
selected_fortune = fortune()
print(f"🥠 {selected_fortune} 🥠")
print("=" * 30)
print("\nMay your day be filled with joy!\n")