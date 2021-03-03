# 40P
# 2) Get from input two different times in the format dd:hh:mm:ss and print
# the difference in seconds between them. The convert the result back to the initial
# format and print that also
# dd is number of days
# hh is number of hours (00-23)
# mm is number od minutes (00-59)
# ss is number of seconds (00-59)


#Input the start and end time
start_time = str(input("Start time in format dd:hh:mm:ss: "))
end_time = str(input("End time in format dd:hh:mm:ss: "))


#Split our inputed strings and covert them into integers
start_days = int(start_time[0:2])
start_hours = int(start_time[3:5])
start_mins = int(start_time[6:8])
start_sec = int(start_time[9:])

end_days = int(end_time[0:2])
end_hours = int(end_time[3:5])
end_mins = int(end_time[6:8])
end_sec = int(end_time[9:])


#Convert our new integers into seconds
start_days_sec = start_days * 24 * 3600
start_hours_sec = start_hours * 3600
start_mins_sec = start_mins * 60

end_days_sec = end_days * 24 * 3600
end_hours_sec = end_hours * 3600
end_mins_sec = end_mins * 60

#Create a total of secons for both start and end times
total_start = start_days_sec + start_hours_sec + start_mins_sec + start_sec
total_end = end_days_sec + end_hours_sec + end_mins_sec + end_sec

#Calculate the difference between the start and end time
diff = total_end.__sub__(total_start)

#Convert the difference into the dd:hh:mm:ss format
diff_sec = diff % 60 # The seconds which are part of the final answer
rem_sec = diff - diff_sec # From total seconds substract the extra seconds which are part of the final answer
rem_mins = rem_sec // 60 # Convert the remaining seconds in minutes
diff_mins = rem_mins % 60 # Calculate the extra minutes which are part of the final answer
rem_mins2 = rem_mins - diff_mins # Substract from the minutes,the extra minutes
rem_hours = rem_mins2 // 60 # Convert remaining minutes into remaining hours
diff_hours = rem_hours % 24 # Calculate the extra hours which are part of the final answer
rem_hours2 = rem_hours - diff_hours # Substract the extra hours from the remaining hours
diff_days = rem_hours2 // 24 # Convert the remaining hours into days,which are part of the final answer


#Print the difference in the required format
print("The difference is: " + str(diff_days) + ":" + str(diff_hours) + ":" + str(diff_mins) + ":" + str(diff_sec))







