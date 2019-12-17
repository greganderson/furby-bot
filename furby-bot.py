from random import randint

starters = [
    "What's on your mind?",
    "What's up?",
    "Hey",
    "What problem are you thinking about right now?"
]

responses = [
    "Yeah that's a good point.",
    "Huh, interesting.",
    "What other ways have you tried looking at it?",
    "Hmm, not sure I follow.",
    "I see",
    "Oh yeah interesting.",
    "Yep",
    "Okay yeah",
    "That might work..."
]

response = input("Furby: {}\nYou: ".format(starters[randint(0, len(starters)) - 1]))
while "thank" not in response.lower():
    response = input("Furby: {}\nYou: ".format(responses[randint(0, len(responses)) - 1]))
print("No problem, see ya later!")