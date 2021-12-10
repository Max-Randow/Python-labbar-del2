# Write your code for lab 8d here.
from cal_abstraction import CalendarDay, Time
from settings import CHECK_AGAINST_FACIT

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
    #Output TimeSpanSeq
    output_list = new_time_span_seq()
  
    current = start
    #Convert to a TimeSpanSeq so it's sorted
    for ts in tss_iter_spans(convert_to_tss(cal_day)):
        
        # Kommer behöva hantera speciall fall senare
        if time_precedes(current, ts_start(ts)):
            output_list = tss_plus_span(output_list,
                    new_time_span(current,ts_start(ts)))

            if time_precedes(ts_end(ts), end) or time_equals(ts_end(ts),end):
                current = ts_end(ts)

            else:
                return output_list
                
        else:
            current = ts_end(ts)

    if current != end:
        output_list = tss_plus_span(output_list, new_time_span(current,end))

    return output_list

def convert_to_tss(cal_day: CalendarDay):
    tss = new_time_span_seq()

    for app in cd_iter_appointments(cal_day):
                
        ts = app_span(app)
        tss = tss_plus_span(tss,ts)

    return tss

#TODO Implement this    
def show_free(cal_name : str, day : int, month : str, start : str, end : str):
    pass



cal_day = new_calendar_day(new_day(15),
        [new_appointment(new_time_span(new_time(new_hour(15), new_minute(0)),
            new_time(new_hour(18), new_minute(0))), new_subject("fuck you")), 
        new_appointment(new_time_span(new_time(new_hour(9), new_minute(30)),
            new_time(new_hour(15), new_minute(0))), new_subject("fuck you 2"))])


print(free_spans(cal_day, new_time(new_hour(10),new_minute(0)),
      new_time(new_hour(20), new_minute(0))))                
