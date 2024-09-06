import random

logo = """


,---.     |    |                             
|__. ,---.|    |    ,---.. . .,---.,---.,---.
|    |   ||    |    |   || | ||---'|    `---.
`    `---'`---'`---'`---'`-'-'`---'`    `---'

 
"""
print(logo)
                                        
data = [
    {"name": "Instagram", "follower_count": 346, "description": "Social media platform", "country": "United States"},
    {"name": "Cristiano Ronaldo", "follower_count": 215, "description": "Footballer", "country": "Portugal"}
]

def format_data(account):
  """Take the account data and returns the printable format"""
  account_name = account["name"]
  account_descr = account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
  """Checks followers against user's guess"""

  if a_followers > b_followers:
    return guess == "a"
  elif b_followers > a_followers:
    return guess == "b"
  else:
    return False

account_a = random.choice(data)
account_b = random.choice(data)
while account_a == account_b:
  account_b = random.choice(data)

print(f"Compare A: {format_data(account_a)}")
print(f"Compare B: {format_data(account_b)}")

score = 0

#ask user for a guess
guess = input("Who has more followers? Type 'A' or 'B':").strip().lower()
#check if user is correct
##get follower count of each account
a_follower_count = account_a["follower_count"]
b_follower_count = account_b["follower_count"]
is_correct = check_answer(guess, a_follower_count, b_follower_count)

#score keeping
if is_correct:
  score += 1
  print(f"You're right! Current score: {score}")

else:
  print(f"Sorry, that's wrong. Final score: {score}")



              


