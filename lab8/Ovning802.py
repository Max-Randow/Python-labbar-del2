from cal_abstraction import *
from cal_ui import *

#Skapa klockslaget (Time) 13:15 och lagra värdet i den globala variablen t1315.
t1315 = Time(Hour(13),Minute(15))

#Skapa tidsperioden (TimeSpan) 13:15-15:00 och lagra värdet i den globala variabeln ts1315.
ts1315 = TimeSpan(t1315,Time(Hour(15),Minute(00)))

"""Skapa en tom CalendarDay och lägg sedan till två möten: ett kl 8:15-9:30 för "Redovisning av uppgift",
 samt ett 13:15-15:00 med "Seminarium i Python". Lagra värdet i den globala variabeln cd15."""

cd15 = new_calendar_day(Day(1))

ts1 = TimeSpan(Time(Hour(8),Minute(15)),Time(Hour(9),Minute(30)))

cd15.appointments.append(Appointment(ts1,Subject("Redovisning av uppgift")))
cd15.appointments.append(Appointment(ts1315,Subject("Seminarium i Python")))

#Print the Calendar Day!
show_cd(cd15)