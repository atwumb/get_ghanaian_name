"""
 Returns the user's Ghana name and meaning the corresponds to their birthdate.
"""

import date_week_born

def get_ghname():
    """
    Returns the Ghanaian name of the user when based on inputted birthdate. When user answers yes, the meaning of the name will be displayed
    """
    birthday_str = input('Enter birthday (format mm/dd/yyyy): ')
    gender = input('Enter your gender (male or female): ')
    bth_weekday = date_week_born.get_day(birthday_str)

    #Place Day and Name in dictonaries, one for male and female
    fem_gh_name = {"Monday": "Adwoa", "Tuesday": "Abena", "Wednesday": "Akua", "Thursday": "Yaa", "Friday": "Afua", "Saturday": "Ama", "Sunday": "Akosua"}
    male_gh_name = {"Monday": "Kwadwo/Kojo", "Tuesday": "Kwabena", "Wednesday": "Kwaku", "Thursday": "Yaw", "Friday": "Kofi", "Saturday": "Kwame", "Sunday": "Akwasi/Kwesi"}

    print("You were born on a %s" % bth_weekday)

    # Based on gender,  return the name that corresponds to birthdate

    if gender == 'female':
        print("Since you were born on %s, your Akan name is %s" % (bth_weekday, fem_gh_name[bth_weekday]))
    else:
        print("Since you were born on %s, your Akan name is %s" % (bth_weekday, male_gh_name[bth_weekday]))

    choice = input("Would you like to know the meaning of your Akan name (y or n): ")
    while True:
        try:
            if choice == 'n':
                print("Maybe next time %s" % (fem_gh_name[bth_weekday]))

            else:
                if gender == 'female':
                    print("The meaning of  %s is %s." % (fem_gh_name[bth_weekday], (get_name_meaning(bth_weekday).lower())))
                else:
                    print("The meaning of  %s is %s." % (male_gh_name[bth_weekday], (get_name_meaning(bth_weekday).lower())))

            break
        except choice not in('y', 'n'):
            print("Please enter a valid answer(y or n)")
            choice = input("Would you like to know the meaning of your Akan name (y or n): ")
    return fem_gh_name[bth_weekday]


def get_name_meaning(week_day):
   """
   Return the meaning of user's name based on the week_day parameter
   """

   dict_meaning = {'Tuesday': "Full of fire and determination, inspirer, risk-taker, will go through a period of uncertainty that will lead to change", "Monday": "The peacemaker, calm and cool, satisfied when doing things to help others, rarely bored""", "Wednesday": "Loving, able to bring people together, don’t prioritize work over people",
   "Thursday": "Strong-willed and powerful leader, engages in social and political resistance", "Friday": "An adventurous wanderer, full of growth, creative, will find purpose in an accidental situation",  "Saturday":"Wise, gentle, happy, able to bring peace in troublesome situations, reinvigorated by spiritual experiences and will become involved in a major cause", "Sunday": "A born leader in bringing people together,  protective of friends and family"}

   return dict_meaning[week_day]


if __name__ == '__main__':
    get_ghname()




