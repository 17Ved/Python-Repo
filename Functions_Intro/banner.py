def banner_text(text: str = " ", screen_width: int = 80) -> None:     # here we're specifying default value 80 to screen width
    # so that's default parameter values, u provide the default value after the parameter name, using the equal symbol
    # if width is shorter than usual, then we will crash program using 'raise Value error'
    if len(text) > screen_width - 4:
        raise ValueError("string {0} is longer than specified width {1}"
                         .format(text, screen_width))

        # here, keyword 'Raise'- that's how you raise an exception in python
        # next we specify the type of exception that we want to raise.
        # value error is good choice here, because the problem caused by one of the values that were passed to our function.
        # Value Error exception is raised when - an operation or function receives an argument that has the right type but an inappropriate value

        # print("EEK!!")
        # print("THE TEXT IS TOO LONG TO FIT IN THE SPECIFIED WIDTH")

    if text == "*":
        print("*" * screen_width)

    else:
        centered_text = text.center(screen_width)
        output_string = "**{0}**".format(centered_text)
        print(output_string)


banner_text("*", 80)
banner_text("Always look on the bright side of life...", 80)
banner_text("If life seems jolly rotten,", 80)
banner_text("There's something you've forgotten!,", 80)
banner_text("And that's to laugh and smile and dance and sing,", 80)
banner_text(screen_width=80)         # we're using keyword argument here, we can specify which parameter we want that 80 argument to be used for, by naming it
banner_text("When you've feeling in the dumps", 80)
banner_text("Don't be silly chumps", 80)
banner_text("Just purse your lips and whistle -  that's the thing", 80)
banner_text("And... always look on the bright side of life...", 80)
banner_text("*", 80)


# result = banner_text("Nothing is returned")
# print(result)
#
#
# number = [4, 2, 7, 5, 8, 9, 10, 3, 1]
# print(number.sort())
# print(number)

# so we pass an asterisk to function, when the function gets an asterisk, it prints a row of asterisk


# when you define a function to have positional arguments, the arguments are assgined to the parameters in their corresponding position
# if you want to a function to return a value, use the return keyword to specify the value that should be returned
# not all function returns something useful- some functions perform an action, rather than producing a value.
# if you don't return a value, python will automatically return None.
# Funcitons that perform an action, rather than returning a value, used to called procedures, but that distinction is no longer made, in modern programming language.










# if a funtion defines 2 positional parameters, then you must provide 2 arguments when calling it.
# UNLESS the parameters have default values, that is. If you provide a default value for a parameter, then
# it's not necessary to provide a corresponding argument to it




# keyword argument
# you can use the parameters as keyword parameters, by specifying the parameter name when you pass the argument
# the default type of parameters, in python are positional or keyword parameters. You can either pass the arguments by their position, or you can
# provide name as the keyword
