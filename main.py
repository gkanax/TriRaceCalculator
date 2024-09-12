import tkinter
import datetime
from tkinter import messagebox
from tkinter import ttk
from tkinter import *

# making of the GUI
window = tkinter.Tk()
window.title("TriPaceCalculator")
window.minsize(width=350, height=250)
window.iconbitmap("tri.ico")
window.grid()

swim_image = PhotoImage(file='swim.PNG')
run_image = PhotoImage(file='run.PNG')
bike_image = PhotoImage(file='bike.PNG')

tabControl = ttk.Notebook(window)
my_gui_style = ttk.Style()
my_gui_style.configure("TNotebook")


tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)


tabControl.add(tab1, text='Swim', image=swim_image, compound="right")
tabControl.add(tab2, text='Bike', image=bike_image, compound="right")
tabControl.add(tab3, text='Run', image=run_image, compound="right")
tabControl.grid(row=0, column=0)


# label for choosing the distance for RUN
my_label_general = tkinter.Label(tab3, text="Choose the distance :", font=("Calibri", 10))
my_label_general.grid(row=0, column=0, columnspan=10, sticky='w', padx=5, pady=5)

# label to enter the desired time for RUN
my_label_general = tkinter.Label(tab3, text="Enter the desired time:", font=("Calibri", 10))
my_label_general.grid(row=0, column=11, columnspan=5, padx=5, pady=5)

# Entry for choosing the hours for RUN
my_entered_hours_run = tkinter.Entry(tab3, width=4)
my_entered_hours_run.insert('end', string="hh:")
my_entered_hours_run.grid(row=1, column=12)

# Entry for choosing the minutes for RUN
my_entered_minutes_run = tkinter.Entry(tab3, width=4)
my_entered_minutes_run.insert('end', string="mm:")
my_entered_minutes_run.grid(row=1, column=13)

# Entry for choosing the seconds for RUN
my_entered_seconds_run = tkinter.Entry(tab3, width=4)
my_entered_seconds_run.insert('end', string="ss")
my_entered_seconds_run.grid(row=1, column=14)

# label for choosing the distance for SWIM
my_label_general = tkinter.Label(tab1, text="Choose the distance :", font=("Calibri", 10))
my_label_general.grid(row=0, column=0, columnspan=10, sticky='w', padx=5, pady=5)

# label to enter the desired time for SWIM
my_label_general = tkinter.Label(tab1, text="Enter the desired time:", font=("Calibri", 10))
my_label_general.grid(row=0, column=11, columnspan=5, padx=5, pady=5)

# Entry for choosing the hours for SWIM
my_entered_hours_swim = tkinter.Entry(tab1, width=4)
my_entered_hours_swim.insert('end', string="hh:")
my_entered_hours_swim.grid(row=1, column=12)

# Entry for choosing the minutes for SWIM
my_entered_minutes_swim = tkinter.Entry(tab1, width=4)
my_entered_minutes_swim.insert('end', string="mm:")
my_entered_minutes_swim.grid(row=1, column=13)

# Entry for choosing the seconds for SWIM
my_entered_seconds_swim = tkinter.Entry(tab1, width=4)
my_entered_seconds_swim.insert('end', string="ss")
my_entered_seconds_swim.grid(row=1, column=14)

# label for choosing the distance for BIKE
my_label_general = tkinter.Label(tab2, text="Choose the distance :", font=("Calibri", 10))
my_label_general.grid(row=0, column=0, columnspan=10, sticky='w', padx=5, pady=5)

# label to enter the desired time for BIKE
my_label_general = tkinter.Label(tab2, text="Enter the desired time:", font=("Calibri", 10))
my_label_general.grid(row=0, column=11, columnspan=5, padx=5, pady=5)

# Entry for choosing the hours for BIKE
my_entered_hours_bike = tkinter.Entry(tab2, width=4)
my_entered_hours_bike.insert('end', string="hh:")
my_entered_hours_bike.grid(row=1, column=12)

# Entry for choosing the minutes for BIKE
my_entered_minutes_bike = tkinter.Entry(tab2, width=4)
my_entered_minutes_bike.insert('end', string="mm:")
my_entered_minutes_bike.grid(row=1, column=13)

# Entry for choosing the seconds for BIKE
my_entered_seconds_bike = tkinter.Entry(tab2, width=4)
my_entered_seconds_bike.insert('end', string="ss")
my_entered_seconds_bike.grid(row=1, column=14)


def on_click():
    messagebox.showerror('RunningPaceCalculator', 'Please fill in the distance!')


def calculate_bike_pace():
    if len(my_entered_hours_bike.get()) == 0 or my_entered_hours_bike.get() == "hh:":
        hours = 0
    else:
        hours = int(my_entered_hours_bike.get())
    if len(my_entered_minutes_bike.get()) == 0 or my_entered_minutes_bike.get() == "mm:":
        minutes = 0
    else:
        minutes = int(my_entered_minutes_bike.get())
    if len(my_entered_seconds_bike.get()) == 0 or my_entered_seconds_bike.get() == "ss":
        seconds = 0
    else:
        seconds = int(my_entered_seconds_bike.get())
    distance = int(radio_state_bike.get())
    if distance == 0:
        on_click()
    bike_total_seconds = hours*3600 + minutes*60 + seconds
    speed = (distance * 3.6)/bike_total_seconds
    format_speed = "{:1.2f}".format(speed)

    # label for pace
    my_label_res_pace = tkinter.Label(tab2, font=("Calibri", 10, "bold"))
    my_label_res_pace.grid(row=5, column=13, columnspan=10, padx=5, pady=5, sticky='w')
    my_label_res_pace.config(text=f"{format_speed}km/h")

    return bike_total_seconds


def calculate_run_pace():
    if len(my_entered_hours_run.get()) == 0 or my_entered_hours_run.get() == "hh:":
        hours = 0
    else:
        hours = int(my_entered_hours_run.get())
    if len(my_entered_minutes_run.get()) == 0 or my_entered_minutes_run.get() == "mm:":
        minutes = 0
    else:
        minutes = int(my_entered_minutes_run.get())
    if len(my_entered_seconds_run.get()) == 0 or my_entered_seconds_run.get() == "ss":
        seconds = 0
    else:
        seconds = int(my_entered_seconds_run.get())
    distance = int(radio_state_run.get())
    if distance == 0:
        on_click()
    run_total_seconds = hours*3600 + minutes*60 + seconds
    distance_per_second = (run_total_seconds * 1000)/distance
    minute = (distance_per_second // 60)
    format_min = "{:1.0f}".format(minute)
    sec = int(distance_per_second % 60)
    format_sec = "{:02d}".format(sec)
    # label for pace
    my_label_res_pace = tkinter.Label(tab3, font=("Calibri", 10, "bold"))
    my_label_res_pace.grid(row=5, column=13, columnspan=10, padx=5, pady=5, sticky='w')
    my_label_res_pace.config(text=f"{format_min}:{format_sec}/km")


def calculate_swim_pace():
    if len(my_entered_hours_swim.get()) == 0 or my_entered_hours_swim.get() == "hh:":
        hours = 0
    else:
        hours = int(my_entered_hours_swim.get())
    if len(my_entered_minutes_swim.get()) == 0 or my_entered_minutes_swim.get() == "mm:":
        minutes = 0
    else:
        minutes = int(my_entered_minutes_swim.get())
    if len(my_entered_seconds_swim.get()) == 0 or my_entered_seconds_swim.get() == "ss":
        seconds = 0
    else:
        seconds = int(my_entered_seconds_swim.get())

    distance = int(radio_state_swim.get())
    if distance == 0:
        on_click()
    swim_total_seconds = hours * 3600 + minutes * 60 + seconds
    distance_per_second = (swim_total_seconds * 100) / distance
    minute = (distance_per_second // 60)
    format_min = "{:1.0f}".format(minute)
    sec = int(distance_per_second % 60)
    format_sec = "{:02d}".format(sec)
    # label for pace
    my_label_res_pace = tkinter.Label(tab1, font=("Calibri", 10, "bold"))
    my_label_res_pace.grid(row=5, column=13, columnspan=10, padx=5, pady=5, sticky='w')
    my_label_res_pace.config(text=f"{format_min}:{format_sec}/100m")


def sum_all_time_fields():
    if len(my_entered_hours_run.get()) == 0 or my_entered_hours_run.get() == "hh:":
        run_hours = 0
    else:
        run_hours = int(my_entered_hours_run.get())
    if len(my_entered_minutes_run.get()) == 0 or my_entered_minutes_run.get() == "mm:":
        run_minutes = 0
    else:
        run_minutes = int(my_entered_minutes_run.get())
    if len(my_entered_seconds_run.get()) == 0 or my_entered_seconds_run.get() == "ss":
        run_seconds = 0
    else:
        run_seconds = int(my_entered_seconds_run.get())
    if len(my_entered_hours_bike.get()) == 0 or my_entered_hours_bike.get() == "hh:":
        bike_hours = 0
    else:
        bike_hours = int(my_entered_hours_bike.get())
    if len(my_entered_minutes_bike.get()) == 0 or my_entered_minutes_bike.get() == "mm:":
        bike_minutes = 0
    else:
        bike_minutes = int(my_entered_minutes_bike.get())
    if len(my_entered_seconds_bike.get()) == 0 or my_entered_seconds_bike.get() == "ss":
        bike_seconds = 0
    else:
        bike_seconds = int(my_entered_seconds_bike.get())
    if len(my_entered_hours_swim.get()) == 0 or my_entered_hours_swim.get() == "hh:":
        swim_hours = 0
    else:
        swim_hours = int(my_entered_hours_swim.get())
    if len(my_entered_minutes_swim.get()) == 0 or my_entered_minutes_swim.get() == "mm:":
        swim_minutes = 0
    else:
        swim_minutes = int(my_entered_minutes_swim.get())
    if len(my_entered_seconds_swim.get()) == 0 or my_entered_seconds_swim.get() == "ss":
        swim_seconds = 0
    else:
        swim_seconds = int(my_entered_seconds_swim.get())

    total_time_in_seconds = (run_hours + bike_hours + swim_hours)*3600 + \
                            (run_minutes + bike_minutes + swim_minutes) * 60 \
                            + bike_seconds + run_seconds + swim_seconds
    total_time = str(datetime.timedelta(seconds=total_time_in_seconds))
    # label for total time
    my_label_res = tkinter.Label(text=f'Total expected time without T1,T2 is: {total_time}',
                                 font=("Calibri", 10, "italic"))
    my_label_res.grid(row=7, column=0, columnspan=5, padx=5, pady=5, sticky='w')


def clear_fields():
    my_entered_seconds_run.delete(0, 'end')
    my_entered_minutes_run.delete(0, 'end')
    my_entered_hours_run.delete(0, 'end')

    my_entered_seconds_swim.delete(0, 'end')
    my_entered_minutes_swim.delete(0, 'end')
    my_entered_hours_swim.delete(0, 'end')

    my_entered_hours_bike.delete(0, 'end')
    my_entered_minutes_bike.delete(0, 'end')
    my_entered_hours_bike.delete(0, 'end')


# making of the calculate button RUN
my_calculate_button = tkinter.Button(tab3, text="Calculate", font=("Calibri", 10),
                                     command=lambda: [calculate_run_pace(), sum_all_time_fields()])
my_calculate_button.grid(row=4, column=10)

# making of the clear button RUN
my_clear_button = tkinter.Button(tab3, text="  Clear  ", font=("Calibri", 10), command=clear_fields)
my_clear_button.grid(row=4, column=13, columnspan=5)

# label for pace RUN
my_label_res = tkinter.Label(tab3, text="Your pace should be:", font=("Calibri", 10, "italic"))
my_label_res.grid(row=5, column=9, columnspan=10, padx=5, pady=5, sticky='w')

# making of the calculate button SWIM
my_calculate_button = tkinter.Button(tab1, text="Calculate", font=("Calibri", 10),
                                     command=lambda: [calculate_swim_pace(), sum_all_time_fields()])
my_calculate_button.grid(row=4, column=10)

# making of the clear button SWIM
my_clear_button = tkinter.Button(tab1, text="  Clear  ", font=("Calibri", 10), command=clear_fields)
my_clear_button.grid(row=4, column=13, columnspan=5)

# label for pace BIKE
my_label_res = tkinter.Label(tab1, text="Your pace should be:", font=("Calibri", 10, "italic"))
my_label_res.grid(row=5, column=9, columnspan=10, padx=5, pady=5, sticky='w')

# making of the calculate button BIKE
my_calculate_button = tkinter.Button(tab2, text="Calculate", font=("Calibri", 10),
                                     command=lambda: [calculate_bike_pace(), sum_all_time_fields()])
my_calculate_button.grid(row=4, column=10)

# making of the clear button BIKE
my_clear_button = tkinter.Button(tab2, text="  Clear  ", font=("Calibri", 10), command=clear_fields)
my_clear_button.grid(row=4, column=13, columnspan=5)

# label for pace BIKE
my_label_res = tkinter.Label(tab2, text="Your pace should be:", font=("Calibri", 10, "italic"))
my_label_res.grid(row=5, column=9, columnspan=10, padx=5, pady=5, sticky='w')


# Radiobutton for RUN
def radio_used():

    print(radio_state_run.get())


# Variable to hold on to which radio button value is checked.
radio_state_run = tkinter.IntVar()
radiobutton1 = tkinter.Radiobutton(tab3, text="5km", value=5000, variable=radio_state_run, command=radio_used)
radiobutton1.grid(row=1, column=0, sticky='w')
radiobutton2 = tkinter.Radiobutton(tab3, text="10km", value=10000, variable=radio_state_run, command=radio_used)
radiobutton2.grid(row=2, column=0, sticky='w')
radiobutton3 = tkinter.Radiobutton(tab3, text="15km", value=15000, variable=radio_state_run, command=radio_used,
                                   anchor="e")
radiobutton3.grid(row=3, column=0, sticky='w')
radiobutton4 = tkinter.Radiobutton(tab3, text="21,1km", value=21100, variable=radio_state_run, command=radio_used)
radiobutton4.grid(row=4, column=0, sticky='w')
radiobutton5 = tkinter.Radiobutton(tab3, text="30km", value=30000, variable=radio_state_run, command=radio_used,
                                   anchor="e")
radiobutton5.grid(row=5, column=0, sticky='w')
radiobutton6 = tkinter.Radiobutton(tab3, text="42,195km", value=42195, variable=radio_state_run,
                                   command=radio_used, anchor="e")
radiobutton6.grid(row=6, column=0, sticky='w')


# Radiobutton for SWIM
def radio_used():
    print(radio_state_swim.get())


# Variable to hold on to which radio button value is checked.
radio_state_swim = tkinter.IntVar()
radiobutton1 = tkinter.Radiobutton(tab1, text="750m", value=750, variable=radio_state_swim, command=radio_used)
radiobutton1.grid(row=1, column=0, sticky='w')
radiobutton2 = tkinter.Radiobutton(tab1, text="1500m", value=1500, variable=radio_state_swim, command=radio_used)
radiobutton2.grid(row=2, column=0, sticky='w')
radiobutton3 = tkinter.Radiobutton(tab1, text="1900m", value=1900, variable=radio_state_swim, command=radio_used,
                                   anchor="e")
radiobutton3.grid(row=3, column=0, sticky='w')
radiobutton4 = tkinter.Radiobutton(tab1, text="3800m", value=3800, variable=radio_state_swim, command=radio_used)
radiobutton4.grid(row=4, column=0, sticky='w')
radiobutton5 = tkinter.Radiobutton(tab1, text="5K", value=5000, variable=radio_state_swim, command=radio_used,
                                   anchor="e")
radiobutton5.grid(row=5, column=0, sticky='w')
radiobutton6 = tkinter.Radiobutton(tab1, text="10K", value=10000, variable=radio_state_swim, command=radio_used,
                                   anchor="e")
radiobutton6.grid(row=6, column=0, sticky='w')


# Radiobutton for SWIM
def radio_used():
    print(radio_state_bike.get())


# Variable to hold on to which radio button value is checked.
radio_state_bike = tkinter.IntVar()
radiobutton1 = tkinter.Radiobutton(tab2, text="20km", value=20000, variable=radio_state_bike, command=radio_used)
radiobutton1.grid(row=1, column=0, sticky='w')
radiobutton2 = tkinter.Radiobutton(tab2, text="40km", value=40000, variable=radio_state_bike, command=radio_used)
radiobutton2.grid(row=2, column=0, sticky='w')
radiobutton3 = tkinter.Radiobutton(tab2, text="90km", value=90000, variable=radio_state_bike, command=radio_used,
                                   anchor="e")
radiobutton3.grid(row=3, column=0, sticky='w')
radiobutton4 = tkinter.Radiobutton(tab2, text="180km", value=180000, variable=radio_state_bike, command=radio_used)
radiobutton4.grid(row=4, column=0, sticky='w')

window.mainloop()
