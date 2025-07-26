task = str(input("Enter Your taks: "))
priority = str(input("Priority (high/medium/low): ")).lower()
time_bound = str(input("Is it time-bound? (yes/no): ")).lower()

reminder = " "

match priority:
    case "high":
         reminder = (task, "is a high priority task that requires immediate attention today!")
      #    if time_bound=="yes":
          #     print("Reminder:", reminder)


    case "Medium":
          reminder = (task, "is a Medium priority task that requires  attention with in the given time frame!")
       #    if time_bound=="yes":

            #   print("Reminder:", reminder)

    case "Low":
          reminder = (task, "is a low priority task. Consider completing it when you have free time.")
       #    if time_bound=="no":
         #      print("Note:", reminder)    




# Add time-sensitivity

if time_bound == "yes":
           
        
       reminder += " that requires immediate attention today!"
elif time_bound == "no":
       
        
       reminder += ". Consider completing it when you have free time."
else:
        reminder += ". Time-sensitivity not recognized."

       

    # Output reminder


#opt =  (reminder + (res))


print("Reminder:", reminder)


