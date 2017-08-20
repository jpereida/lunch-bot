import random

messages = [
        "Good morning!",
        "Hey!",
        "This sounds good!",
        "Sounds delicious!",
        "Yesss!",
        "Hello!"
]

def RandomMessage():
    return random.choice(messages) + " "

def SingleItemLunchMessage(item):
    msg = '{}Today''s menu is {}'.format(RandomMessage(), item)
    return msg

def MultiItemLunchMessage(items):
    msg = '{}Today''s menu:\n Option 1: {}\n Option 2: {}'.format(RandomMessage(), items[0], items[1])
    return msg

def LunchMessage(items):
    msg = '';

    if len(items) == 1:
        msg = SingleItemLunchMessage(items[0])
    else:
        msg = MultiItemLunchMessage(items)

    return msg
        

    