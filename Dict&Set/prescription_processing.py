from priscription_data import patients
# when popping items from the sets, there's a slight difference. Set's aren't indexable, so the set pop method doesn't
# take any argument.
# it pops an arbitrary item from the set, and returns that item.

trial_patients = {"Denise", "Eddie", "Frank", "Georgia", "Kenny"}

while trial_patients:
    patient = trial_patients.pop()
    print(patient, end=" : ")
    prescription = patients[patient]
    print(prescription)
