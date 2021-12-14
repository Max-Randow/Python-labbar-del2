# Write your code for lab 8d here.
from cal_abstraction import CalendarDay, Time
from settings import CHECK_AGAINST_FACIT
from cal_ui import get_calendar
from cal_output import show_ts,show_day_heading
if CHECK_AGAINST_FACIT:
    try:
        from facit_la8_uppg import TimeSpanSeq
    except:
        print("*" * 100)
        print("*" * 100)
        print("Kan inte hitta facit; ändra CHECK_AGAINST_FACIT i test_driver.py till False")
        print("*" * 100)
        print("*" * 100)
        raise
else:
    from lab8b import *


def free_spans(cal_day: CalendarDay, start: Time, end: Time) -> TimeSpanSeq:
    
    # Ensure correct types
    ensure_type(cal_day, CalendarDay)
    ensure_type(start, Time)
    ensure_type(end, Time)
    
    output_tss = new_time_span_seq()
    current  = start
   
    for app in cd_iter_appointments(cal_day):
        ts = app_span(app)

        if time_precedes_or_equals(current, ts_start(ts)) and time_precedes(ts_start(ts),end):
            #Current is before the appointment's start time.
            
            #Checks so that the two times are not equal and that the current time is after start
            if not time_equals(current,ts_start(ts)) and time_precedes(start,current):

                #TODO Change this
                
                #If end is before ts_Start(), we enter this 
                if time_precedes(end,ts_start(ts)):
                    output_tss = tss_plus_span(output_tss,new_time_span(current,end))
                    #We are done.
                    return output_tss
                #Otherwise add it like normal
                output_tss = tss_plus_span(output_tss,new_time_span(current,ts_start(ts)))
      
            #Set current to the end of the appointment
            current = ts_end(ts)

    
    if time_precedes(current,end):
        output_tss = tss_plus_span(output_tss,new_time_span(current,end))
    
    return output_tss

def show_free(cal_name : str, day : int, month : str, start : str, end : str):
     #Turn the parameters into our data types.
    day = new_day(day)
    month = new_month(month)
    start_time = new_time_from_string(start)
    end_time = new_time_from_string(end)

    cal_year = get_calendar(cal_name)
    cal_month = cy_get_month(month,cal_year)
    cal_day = cm_get_day(cal_month,day)

    tss = free_spans(cal_day,start_time,end_time)
    
    for ts in tss_iter_spans(tss):
        show_ts(ts)
        print()



#(For testing code)
from cal_ui import book,show,create 

#--- TEST CODE ----#
create("Jayne")

book("Jayne", 20, "sep", "12:00", "14:00", "Rob train")

book("Jayne", 20, "sep", "15:00", "16:00", "Escape with loot")

show("Jayne", 20, "sep")

show_free("Jayne", 20,"sep","14:30","14:31")