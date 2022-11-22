import random

class NoHealth (Exception):
    def __init__(self, message = "Person Is Dead"):
        Exception.__init__(self, message)


class NoMood (Exception):
    def __init__(self, message = "Person Is In Depression"):
        Exception.__init__(self, message)


class NoMoney (Exception):
    def __init__(self, message = "Person Doesn't Have Any Money"):
        Exception.__init__(self, message)

class Action:
    name = ""
    health = 0
    mood = 0
    money = 0.0
    def __init__(self, name, health, mood, money):
        self.name = name
        self.health = health
        self.mood = mood
        self.money = money


class Work(Action):
    def __init__(self, name, health, mood, money):
        Action.__init__(self, name, health, mood, money)

class Rest(Action):
    def __init__(self, name, health, mood, money):
        Action.__init__(self, name, health, mood, money)



class Person:
    name = ""
    health = 0
    mood = 0
    money = 0.0
    def __init__(self, name = "", health = 0, mood = 0, money = 0):
        self.name = name
        self.health = health
        self.mood = mood
        self.money = money




    def __str__(self):
        return f"==={self.name}===\n" \
               f"health = {self.health}\n" \
               f"mood = {self.mood}\n" \
               f"money = {self.money}\n"
    def change_state(self, health, mood, money):
        self.health += health
        self.mood += mood
        self.money += money

        if self.health < 0:
            raise NoHealth

        if self.mood < 0:
            raise NoMood

        if self.money < 0:
            raise NoMoney




    def do(self, action: Action):
        if type(action == Action):
            self.change_state(action.health, action.mood, action.money)
        if type(action == Work):
            if self.mood > 90:
                self.change_state(action.health, action.mood, action.money + ((action.money / 100) * 10))
            else:
                self.change_state(action.health, action.mood, action.money)
        if type(action == Rest):
            self.change_state(action.health, action.mood, action.money)




people = [Person, Person, Person]
people[0] = Person("Rogalik", 52, 47, 88)
people[1] = Person("Churchhela", 78, 50, 91)
people[2] = Person("Bublik", 89, 12, 36)
actions = [Action, Action, Action]
actions[0] = Rest("Bar", -10, 20, -20)
actions[1] = Action("Supermarket", -30, -8, -50)
actions[2] = Action("Factory", 30, -20, 40)
print(people[0])

while True:
    try:
        r_p = random.randint(0,2)
        people[r_p].do(actions[random.randint(0,2)])
        print(people[r_p])
    except(NoMoney):
        print(f"Person Doesn't Have Money")
        break
    except (NoMood):
        print(f"Person is In Depression")
        break
    except (NoHealth):
        print(f"Person Is Dead\n")
        break
    except (Exception) as error:
        print(f"Error: {error}")
        break
        print(people[0], people[1], people[2])




