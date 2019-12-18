from random_item_list import RandomItemList
import time

starter_messages = []
with open('furby-greetings.txt', 'r') as f:
    starter_messages = f.read().split('\n')
starters = RandomItemList(starter_messages)

response_messages = []
with open('furby-responses.txt', 'r') as f:
    response_messages = f.read().split('\n')
responses = RandomItemList(response_messages)

typing_ellipsis = [
    "Furby: .",
    "Furby: ..",
    "Furby: ...",
]

def typing(s):
    # Determine how long to do the typing ellipsis, but at least do 3
    time_for_ellipsis = max(int(len(s) / 7), 3)

    print("\nFurby: ", end='')
    time.sleep(.1)

    for i in range(time_for_ellipsis):
        if i % len(typing_ellipsis) == 0:
            # Reset the line
            print("\rFurby: .  ", end='')
        print("\r{}".format(typing_ellipsis[i % len(typing_ellipsis)]), end='')
        time.sleep(.5)
    print("\r             ")

start = starters.next_item()
typing(start)
user_response = input("Furby: {}\nYou: ".format(start))

# Keep the friendly conversation going
while "thank" not in user_response.lower():
    furby_response = responses.next_item()
    typing(furby_response)
    user_response = input("Furby: {}\nYou: ".format(furby_response))
    time.sleep(.5)

end = "Furby: No problem, see ya later!"
typing(end)
print(end)