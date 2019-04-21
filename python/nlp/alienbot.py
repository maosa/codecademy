##### CODECADEMY PROJECT
##### ALIENBOT

##### importing regex and random libraries
import re
import random

##### potential negative responses
negative_responses = ("no", "nope", "nah", "naw", "not a chance", "sorry")
##### keywords for exiting the conversation
exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")
##### random starter questions
random_questions = (
    "Why are you here? ",
    "Are there many humans like you? ",
    "What do you consume for sustenance? ",
    "Is there intelligent life on this planet? ",
    "Does Earth have a leader? ",
    "What planets have you visited? ",
    "What technology do you have on this planet? "
    )


alienbabble = (
    ##### Your planet...
    {r'.*\s*your planet':
        ("My planet is a utopia of diverse organisms and species. ",
        "I am from Opidipus, the capital of the Wayward Galaxies. ")
    },
    ##### why do you...?
    {r'why\sdo\syou\s(.*[^\?]*)\??':
        ("What makes you think I {0}? ",
        "Do I {0}?",
        "Do you think I should {0}? ")
    },
    ##### why...?
    {r'.*why\s+.*':
        ("I come in peace. ",
        "I am here to collect data on your planet and its inhabitants. ",
        "I heard the coffee is good. ")
    },
    ##### what...?
    {r'.*what\s+.*':
        ("Why do you ask? ",
        "What do you think? ")
    },
    ##### it is...
    {r'.*it\s+is':
        ("You seem very certain. Why is that? ",
        "Do you have any evidence? ")
    },
    ##### I think...
    {r'.*i\s+think\s(.*)[\?\.\!]?':
        ("But you're not sure {0}? ",
        "Why do you think {0}? ")
    },
    ##### Other responses
    {r'.*':
        ("Please tell me more. ",
        "Tell me more! ",
        "Why do you say that? ",
        "I see. Can you elaborate? ",
        "Interesting. Can you tell me more? ",
        "I see. How do you think? ",
        "Why? ",
        "How do you think I feel when you say that? ")
    }
)


##### Define greet() below:
def greet():
    name = input("Hello human! What is your name? ")
    will_help = input("Hi {}, I'm Etcetera. I'm not from this planet. Will you help me learn about your planet? ".format(name))
    if will_help in negative_responses:
        print("Ok, have a nice Earth day!")
        return
    else:
        return True


##### Define make_exit() here:
def make_exit(reply):
    for exit_command in exit_commands:
        if exit_command == reply:
            print("Bye bye human! I'm off to my galaxy...")
            return True


##### Define alienbot() next:
def alienbot():
    if greet():
        reply = input(random.choice(random_questions)).lower()
        while make_exit(reply) is not True:
            reply = converse(reply)


##### Define converse() below:
def converse(reply):
    for pair in alienbabble:
        for regex_pattern, alien_answers in pair.items():
            found_match = re.match(regex_pattern, reply)
            ##### re.match() returns either a the matching text or None if no match is found
            if found_match:
                alien_answer = random.choice(alien_answers)

    formatted_alien_answer = alien_answer.format(*[reflect(matching_group) for matching_group in found_match.groups()])
    ##### The * operator tells the function that there may or may not be one or more arguments (we dont know how many) to be interpolated into the string. These arguments will correspond to the Regex groups weve captured from the alienbabble response pairs. Not every response pair in alienbabble has a regex group. This is why we need the * operator.
    reply = input(formatted_alien_answer).lower()
    return reply

##### dictionary used to switch pronouns and verbs in responses
reflections = {
    "i'm" : "you are",
    "you're" : "i'm",
    "was" : "were",
    "i" : "you",
    "are" : "am",
    "am" : "are",
    "i'd" : "you would",
    "i've" : "you have",
    "i'll" : "you will",
    "my" : "your",
    "you've" : "I have",
    "you'll" : "I will",
    "your" : "my",
    "yours" : "mine",
    "you" : "I",
    "me" : "you"
}


def reflect(response):
  words = response.split()
  for index, word in enumerate(words):
    if word in reflections:
      words[index] = reflections[word]
  return ' '.join(words)

alienbot()
