"""
Homework 2
Create 5 dictionaries. Each dictionary should represent a CV.
Create a CV containing the information of the 5 created people.
Print the information on CVs created on the screen.
"""

mehmet_cv = {"Name": "Mehmet",
             "Surname": "Altın",
             "Age": 34,
             "Gender": "Male",
             "Job": "Doctor",
             "Job experience": "5 Years",
             "Language": "English"}

ahmet_cv = {"Name": "Ahmet",
            "Surname": "Demir",
            "Age": 25,
            "Gender": "Male",
            "Job": "Engineer",
            "Job experience": "1 Year",
            "Language": "Turkish"}

alper_cv = {"Name": "Alper",
            "Surname": "Bakır",
            "Age": 22,
            "Gender": "Male",
            "Job": "Cashier",
            "Job experience": "2 Years",
            "Language": "Russian"}

nehir_cv = {"Name": "Nehir",
            "Surname": "Civa",
            "Age": 27,
            "Gender": "Female",
            "Job": "Teacher",
            "Job experience": "3 Years",
            "Language": "Turkish"}

ezgi_cv = {"Name": "Ezgi",
           "Surname": "Çelik",
           "Age": 29,
           "Gender": "Female",
           "Job": "Freelancer",
           "Job experience": "2 Years",
           "Language": "English"}

cv_s = [mehmet_cv, ahmet_cv, alper_cv, nehir_cv, ezgi_cv]  # Putting dictionaries in a list

for i in cv_s:  # Looping in a list for dictionaries
    for k, v in i.items():  # Looping in a dictionary for items
        print(f"{k}: {v}")  # Printing the keys and the values
        if not cv_s[-1] == i:  # Getting the  dictionaries in the list except fot the last one
            if k == "Language":  # İf key equals to "languages" key prints the separating line
                print("--" * 12)
