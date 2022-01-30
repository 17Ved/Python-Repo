
# Updating with shelves & common ways to increase performance
# Writeback -- When you use write back python caches the object in memory and doesn't actually update the shelve file itself until you either close the shelveor use to sync method.
# If there's been a lot of changes, closing a shelve can take a while because all have to be written to disk at once.
# There's potential problem with sync method that can catch people out so
# Sync causes Cache to be cleared

import shelve
#
# blt = ["bacon", "lettuce", "tomato", "bread"]
# beans_on_toast = ["beans", "bread"]
# scrambled_eggs = ["egge", "butter", "milk"]
soup = ["tin of soup"]
# pasta = ["pasta", "cheese"]

with shelve.open('recipes', writeback=True) as recipes:
    # recipes["blt"] = blt
    # recipes["beans on toast"] = beans_on_toast
    # recipes["scrambled eggs"] = scrambled_eggs
    # recipes["pasta"] = pasta
    # recipes["soup"] = soup
    #
    # recipes["blt"].append("butter")
    # recipes["pasta"].append("tomato")

    # temp_list = recipes["blt"]
    # temp_list.append("butter")
    # recipes["blt"] = temp_list
    #
    # temp_list = recipes["pasta"]
    # temp_list.append("tomato")
    # recipes["pasta"] = temp_list

    # recipes["soup"].append("croutons")
    recipes["soup"] = soup
    recipes.sync()
    soup.append("cream")

    for snack in recipes:
        print(snack, recipes[snack])
    else:
        None




