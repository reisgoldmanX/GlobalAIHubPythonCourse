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
             "Language": "English"}

ahmet_cv = {"Name": "Ahmet",
            "Surname": "Demir",
            "Age": 25,
            "Gender": "Male",
            "Job": "Engineer",
            "Language": "Turkish"}

alper_cv = {"Name": "Alper",
            "Surname": "Bakır",
            "Age": 22,
            "Gender": "Male",
            "Job": "Cashier",
            "Language": "Russian"}

nehir_cv = {"Name": "Nehir",
            "Surname": "Civa",
            "Age": 27,
            "Gender": "Female",
            "Job": "Teacher",
            "Language": "Turkish"}

ezgi_cv = {"Name": "Ezgi",
           "Surname": "Çelik",
           "Age": 29,
           "Gender": "Female",
           "Job": "Freelancer",
           "Language": "English"}

cv_s = [mehmet_cv, ahmet_cv, alper_cv, nehir_cv, ezgi_cv]

for i in cv_s:
    for k, v in i.items():
        print(f"{k}: {v}")
        if k == "Language":
            if not cv_s[-1] == i:
                print("----------------------")
