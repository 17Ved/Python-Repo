from priscription_data import *

trial_patients = ["Denise", "Eddie", "Frank", "Georgia", "Kenny"]

# Remove Warfarin and add Edoxaban
for patient in trial_patients:
    prescription = patients[patient]
    if warfarin in prescription:
        prescription.remove(warfarin)
        # prescription.discard(warfarin)
        prescription.add(edoxaban)
    else:
        print(f"patient {patient} is not taking Warfarin"
              f"Please remove {patient} from the trial")

    print(patient, prescription)



































