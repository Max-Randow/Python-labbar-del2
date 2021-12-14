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

"""Returns a TimeSpanSequence containing all the free TimeSpans between start and end"""
def free_spans(cal_day: CalendarDay, start: Time, end: Time) -> TimeSpanSeq:
    # Ensure correct types
    ensure_type(cal_day, CalendarDay)
    ensure_type(start, Time)
    ensure_type(end, Time)
    
    #Define variables
    output_tss = new_time_span_seq()
    current = start
   
    for app in cd_iter_appointments(cal_day):
        ts = app_span(app)
        #If the app end is before current (|---|   |c), skip it
        if time_precedes_or_equals(ts_end(ts),current):
            continue
        #If end is before or equal to current  ( |e     |c), break
        if time_precedes_or_equals(end,current):
            break
        #If the app start is after the end (|e   |----| ), add a ts from current to end and break
        if time_precedes_or_equals(end,ts_start(ts)):
            output_tss = tss_plus_span(output_tss,new_time_span(current,end))
            current = end
            break
        #If app start is before current and current is before the app end (|---|c---|), set current to app end
        if time_precedes_or_equals(ts_start(ts), current) and time_precedes_or_equals(current,ts_end(ts)):
            current = ts_end(ts)
        #We know that the app is between current and end (|c   |---|    |e)
        else:
            output_tss = tss_plus_span(output_tss,new_time_span(current,ts_start(ts)))
            current = ts_end(ts)

    #If current is before end (|c   |e) after the loop, we know that we have not added the "last bit". Add it.
    if(time_precedes(current,end)):
        output_tss = tss_plus_span(output_tss,new_time_span(current,end))
    
    #Return the free TimeSpans as a TimeSpanSequence.
    return output_tss

"""An interface function that prints all the free TimeSpans between two times, start and end."""
def show_free(cal_name : str, day : int, month : str, start : str, end : str):
     #Turn the parameters into our data types.
    day = new_day(day)
    month = new_month(month)
    start_time = new_time_from_string(start)
    end_time = new_time_from_string(end)

    cal_year = get_calendar(cal_name)
    cal_month = cy_get_month(month,cal_year)
    cal_day = cm_get_day(cal_month,day)

    #Retrieve all the free TimeSpans.
    tss = free_spans(cal_day,start_time,end_time)
    
    #Print it through the generator.
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

show_free("Jayne", 20,"sep","14:30","14:40")