#Set

#non indexable
#cannot contain duplicate values

numbers = {
            1,2,3,4,5,6,6,4,2,3,6, 
           "Hyderabad", "Hyderabad"
           }

numbers.add(100)




survey_1 = { "Ankith",
            "Vaibhav",
            "Santhosh",
            "Zen",
            "Pascal"   
            }

survey_2 = {
            # "Zen",
            # "Pascal",
            "Jeniffer",
            "Rose",
            "Jaine",
            "Abhishek"
            }


cse_students = {
            "Zen",
            "Pascal",
            "Jeniffer",
            "Rose",
            "Jaine",
            "Abhishek"
            }
             
ai_students = {
             "Jaine",
            "Abhishek",
            "Prashanth"     
                }




common = cse_students.issuperset(ai_students)


print(common)