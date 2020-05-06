# fork modified to show days since first COVID-19 case instead of a countdown to events
import time
import tkinter as tk
import datetime as dt

window_size = '800x480'
line1 = 'Days since four COVID-19 cases in St. Louis MSA:'
date_four_cases = dt.date(2020,3,14)

def tick(time1=''):
    # get the current local time from the PC
    time2 = time.strftime('%H:%M')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        today = dt.date.today()
        cal_day.config(text=today.strftime("%A"))
        cal_day.grid(row=0, column=0, sticky=tk.W)
        cal_date.config(text=today.strftime("%x"))
        cal_date.grid(row=0, column=1, sticky=tk.E)
        clock.config(text=time2)
        clock.grid(row=1, columnspan=2)
        elapsed_time = today - date_four_cases
        elapsed_days = str(elapsed_time.days)
        display_line1.grid(row=2, columnspan=2)
        display_line1.config(text = line1)
        display_line2.grid(row=3, columnspan=2)
        display_line2.config(text = elapsed_days)

    # calls itself every 200 milliseconds
    # to update the time display as needed
    clock.after(200, tick)

root = tk.Tk()
root.configure(background='#7ea0d6')
root.geometry(window_size)
root.columnconfigure(1, weight=1)
root.title('KFW Clock')
cal_day = tk.Label(root, font=('helvetica', 48), bg='#7ea0d6')
cal_date = tk.Label(root, font=('helvetica', 48), bg='#7ea0d6')
clock = tk.Label(root, font=('helvetica', 128, 'bold'), bg='#7ea0d6', fg='blue4')
display_line1 = tk.Label(root, font=('helvetica', 24), bg='#7ea0d6')
display_line2 = tk.Label(root, font=('helvetica', 56, 'bold'), bg='#7ea0d6')

# clock.pack(fill='both', expand=1)
tick()
root.mainloop()
