morning = {'Java', 'C', 'Ruby', 'Lisp', 'C#'}
afternoon = {'Python', 'C#', 'Java', 'C', 'Ruby'}

possible_courses = set(morning) ^ afternoon
# possible_courses = set (morning).symmetric_difference(afternoon)
print(possible_courses)

possible_courses = set(afternoon).symmetric_difference(morning)
print(possible_courses)

# Symmetric Difference ----
# symmetric difference is opposite of intersection
# it introduces the set of items that are in one set or the other, but no in both.


# Subsets & Supersets ---
# When all the items of one set are also in another set, the contained set is called a 'subset' of the containing set.
# 
