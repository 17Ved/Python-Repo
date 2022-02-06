# Getters and Setters in Python ----
# In Python, getters and setters are not the same as those in other object-oriented programming languages.
# Basically, the main purpose of using getters and setters in object-oriented programs is to ensure data encapsulation.
# Private variables in python are not actually hidden fields like in other object-oriented languages.
# Getters and Setters in python are often used when:
# We use getters & setters to add validation logic around getting and setting a value.
# To avoid direct access of a class field i.e. private variables cannot be accessed directly or modified by external user.
# Getter is actually a method that used to get the value of a data attribute.
# Setter is also a method that used to set the value of the class data attribute

class Player(object):           # Convention is that python class name should start with Capital Letter, but some classes don't follow that convention

    def __init__(self, name):
        self.name = name
        self._lives = 3              # these 3 values starts with default values -- lives, level, score
        self._level = 1
        self._score = 0

    def _get_lives(self):
        return self._lives

    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print("Lives cannot be negative")
            self._lives = 0

    def _get_level(self):
        return self._level

    def _set_level(self, level):
        if level > 0:
            delta = level - self._level
            self._score += delta * 100
            self._level = level
        else:
            print("Level can't be less than 1")

    lives = property(_get_lives, _set_lives)                # When you use _get_lives'()', _set_lives'()' -- you are actually calling the method and the property's 'getter' will be set to whatever the result of calling _get_lives is.
    level = property(_get_level, _set_level)                # Given below line is alternate syntax for property line

    @property
    def score(self):                    # we add the @property decorator before the method on the previous line & decorator takes care of the score equals property line (as for lives and lives)
        return self._score

    @score.setter
    def score(self, score):
        self._score = score

    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, Level: {0.level}, Score: {0.score}".format(self)
        # OR
        # return "Name: {0}, Lives: {1}, Level: {2}, Score: {3}".format(self.name, self.lives, self.level, self.score)


# Inheritance - In python, classes can inherit directly form several superclasses, which is known as multiple inheritance
# So, you can write code once, put that code in the Super class and then any class that 'extends' or 'inherits' from - they're the same thing effectively - that class
# is going to be able to take advantage of the properties or methods that are defined in the Super class.


























