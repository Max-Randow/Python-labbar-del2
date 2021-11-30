from cal_ui import *
# Write your code for lab 8C (remove) here.

def remove(calendarName : str, day : int, month  : str, start_time):
    #Hämta kalendern, gå till specifik månad, sedan specifik dag och sedan tar man bort den tid med start tiden vi fått.
    day = new_day(day)
    month = new_month(month)
    start_time = new_time_from_string(start_time)

    cal_year = get_calendar(calendarName)
    cal_month = cy_get_month(month,cal_year)
    cal_day = cm_get_day(cal_month,day)

    # Ensure that the date is proper.  If not, this will raise an exception.
    new_date(day,month)

    appointment = get_appointment(cal_day,start_time)
    if(appointment is not None):
        new_cal_day = cd_remove_appointment(cal_day,appointment)
        new_cal_month = cm_plus_cd(cal_month, new_cal_day)
        new_cal_year = cy_plus_cm(cal_year, new_cal_month)

        insert_calendar(calendarName,new_cal_year)

        print("Appointment removed.")
    else:
        print("There is no appointment to remove.")
    
def get_appointment(day : CalendarDay, start : Time) -> Appointment:
    #Ensure the correct types.
    ensure_type(day,CalendarDay)
    ensure_type(start,Time)

    #Iterate through all the appointments and look for any that starts with our start time.
    for app in cd_iter_appointments(day):
        if(ts_start(app_span(app)) == start):
            #We found it. We now return it as we can only have one appointment during this time.
            return app

def cd_remove_appointment(cal_day : CalendarDay, app : Appointment) -> CalendarDay:
    ensure_type(cal_day,CalendarDay)
    ensure_type(app,Appointment)

    def remove_appointment(app : Appointment, apps : List[Appointment]):
        apps.remove(app)

        return apps


    return CalendarDay(cd_day(cal_day),remove_appointment(app,cal_day.appointments))



#--- TEST CODE ----#
create("Jayne")

book("Jayne", 20, "sep", "12:00", "14:00", "Rob train")

book("Jayne", 20, "sep", "15:00", "16:00", "Escape with loot")

show("Jayne", 20, "sep")

remove("Jayne", 20, "sep", "15:00")

book("Jayne", 20, "sep", "15:00", "16:00", "Return loot")

show("Jayne", 20, "sep")

