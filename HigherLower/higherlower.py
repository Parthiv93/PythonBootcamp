import random,higherlowerart,higherlowerdata,os
def random_account():
    return random.choice(higherlowerdata.data)
def print_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"
def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
def game():
  print(higherlowerart.logo)
  score = 0
  game_should_continue = True
  account_a = random_account()
  account_b = random_account()
  while game_should_continue:
    account_a = account_b
    account_b = random_account()
    while account_a == account_b:
      account_b = random_account()
    print(f"Compare A: {print_data(account_a)}.")
    print(higherlowerart.vs)
    print(f"Against B: {print_data(account_b)}.")
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    os.system('cls')
    print(higherlowerart.logo)
    if is_correct:
      score += 1
      print(f"Correct!! Current score: {score}.")
    else:
      game_should_continue = False
      print(f"Wrong!!. Final score: {score}")
game()