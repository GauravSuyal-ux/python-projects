import random
secret_num = random.randint(1,100)
print(secret_num)
count = 1
print("======Guess the number between 1-100======")
while True:
    guess = int(input("Guess the number: "))

    if guess==secret_num:
        print(f"Yes! that's correct, the number is {secret_num}..",f"You guessed in {count} attempts.")
        break
    elif guess>secret_num:
        print("You guessed the grater one,Try to think the smaller one.. ")
    else:
        print("You guessed the smaller one, Try to think grater number..")
    
    count+=1