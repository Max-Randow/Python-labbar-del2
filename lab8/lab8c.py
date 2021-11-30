#Imports
from cal_abstraction import *
#Book uses these as well.
from cal_ui import get_calendar,insert_calendar
#(For testing code)
from cal_ui import * 
# Write your code for lab 8C (remove) here.

def remove(calendarName : str, day : int, month  : str, start_time : str):
    """Removes an appointment from an existing calendar."""
    
    #Turn the parameters into our data types.
    day = new_day(day)
    month = new_month(month)
    start_time = new_time_from_string(start_time)

    cal_year = get_calendar(calendarName)
    cal_month = cy_get_month(month,cal_year)
    cal_day = cm_get_day(cal_month,day)

    # Ensure that the date is proper.  If not, this will raise an exception.
    new_date(day,month)

    #Get the appointment
    appointment = get_appointment(cal_day,start_time)

    #We only want to enter this if statement if the appointment actually exists
    if(appointment is not None):
        #We now have to recreate the cal_year.
        new_cal_day = cd_remove_appointment(cal_day,appointment)
        new_cal_month = cm_plus_cd(cal_month, new_cal_day)
        new_cal_year = cy_plus_cm(cal_year, new_cal_month)

        #We then insert this as the new year (it replaces the old)
        insert_calendar(calendarName,new_cal_year)

        print("Appointment removed.")
    #Otherwise we want to tell the user that there is no appointment.
    else:
        print("There is no appointment to remove.")
    
def get_appointment(day : CalendarDay, start : Time) -> Appointment:
    """Returns an appointment, given the day and start time"""
    #Ensure the correct types.
    ensure_type(day,CalendarDay)
    ensure_type(start,Time)

    #Iterate through all the appointments and look for any that starts with our start time.
    for app in cd_iter_appointments(day):
        if(ts_start(app_span(app)) == start):
            #We found it. We now return it as we can only have one appointment during this time.
            return app

def cd_remove_appointment(cal_day : CalendarDay, app : Appointment) -> CalendarDay:
    """Removes an appointment and returns the new modified CalendarDay"""
    ensure_type(cal_day,CalendarDay)
    ensure_type(app,Appointment)

    def remove_appointment(app : Appointment, apps : List[Appointment]):
        #Here we remove the Appointment (NOTE: 'Avbokningen får så klart ändra i lagringen av kalendrar' (according to the website))
        apps.remove(app)

        return apps

    #We return a new CalendarDay (is not really necessary but it makes the code more readable)
    return CalendarDay(cd_day(cal_day),remove_appointment(app,cal_day.appointments))



#--- TEST CODE ----#
create("Jayne")

book("Jayne", 20, "sep", "12:00", "14:00", "Rob train")

book("Jayne", 20, "sep", "15:00", "16:00", "Escape with loot")

show("Jayne", 20, "sep")

remove("Jayne", 20, "sep", "15:00")

book("Jayne", 20, "sep", "15:00", "16:00", "Return loot")

show("Jayne", 20, "sep")

