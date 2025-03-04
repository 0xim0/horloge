#import and def variables

from tkinter import*
from datetime import datetime
from pygame import mixer

window = Tk()

#timer
run_timer = False
seconde_timer = 0
hour_timer = 0
minute_timer = 0
hour_timer = 0

#chrono
run_chrono = False
miliseconde_chrono = 0
seconde_chrono = 0
minute_chrono = 0
hour_chrono = 0

#date and time
date_now= 0
time_now = 0

#alarm
run_alarm = False
alarm_counter = 0
minute_alarm = 0
hour_alarm = 0
time_alarm0 = 0
time_alarm1 = 0
time_alarm2 = 0
time_alarm3 = 0
time_alarm4 = 0
time_alarm5 = 0
time_alarm6 = 0
time_alarm7 = 0
time_alarm8 = 0
time_alarm9 = 0
time_now_alarm = 0

#easter egg
go_home_counter = 0

window.state('zoomed')

for i in range(11):  # Nombre de lignes
    window.grid_rowconfigure(i, weight=1)  # Ajuste la hauteur des lignes
for j in range(9):  # Nombre de colonnes
    window.grid_columnconfigure(j, weight=1)  # Ajuste la largeur des colonnes


#home

def go_home():
    
    #easter egg
    global go_home_counter
    go_home_counter += 1
    if go_home_counter == 10:
        mixer.init()
        sound = mixer.Sound("easter_egg.mp3")
        sound.play()
        go_home_counter = 0
        
    #timer
    bouton_seconde_timer.grid_remove()
    bouton_seconde_10_timer.grid_remove()
    bouton_seconde_moins_1_timer.grid_remove()
    bouton_seconde_moins_10_timer.grid_remove()
    bouton_minute_timer.grid_remove()
    bouton_minute_10_timer.grid_remove()
    bouton_minute_moins_1_timer.grid_remove()
    bouton_minute_moins_10_timer.grid_remove()
    affichage_timer.grid_remove()
    bouton_start_timer.grid_remove()
    bouton_stop_timer.grid_remove()
    bouton_restart_timer.grid_remove()
    bouton_go_timer.grid()

    #chrono
    affichage_chrono.grid_remove()
    bouton_start_chrono.grid_remove()
    bouton_stop_chrono.grid_remove()
    bouton_restart_chrono.grid_remove()
    bouton_go_chrono.grid()

    #date and time
    affichage_date_heure.grid_remove()
    bouton_go_date_heure.grid()

    #alarm
    bouton_hour_alarm.grid_remove()
    bouton_hour_10_alarm.grid_remove()
    bouton_hour_moins_1_alarm.grid_remove()
    bouton_hour_moins_10_alarm.grid_remove()
    bouton_minute_alarm.grid_remove()
    bouton_minute_10_alarm.grid_remove()
    bouton_minute_moins_1_alarm.grid_remove()
    bouton_minute_moins_10_alarm.grid_remove()
    bouton_create_alarm.grid_remove()
    bouton_create_alarm.grid_remove()
    bouton_confirm_create_alarm.grid_remove()
    affichage_create_alarm.grid_remove()
    affichage_alarm0.grid_remove()
    affichage_alarm1.grid_remove()
    affichage_alarm2.grid_remove()
    affichage_alarm3.grid_remove()
    affichage_alarm4.grid_remove()
    affichage_alarm5.grid_remove()
    affichage_alarm6.grid_remove()
    bouton_go_alarm.grid()

def go():
    global go_home_counter
    go_home_counter = 0
    bouton_go_timer.grid_remove()
    bouton_go_chrono.grid_remove()
    bouton_go_date_heure.grid_remove()
    bouton_go_alarm.grid_remove()

def go_timer():
    bouton_seconde_timer.grid()
    bouton_seconde_10_timer.grid()
    bouton_seconde_moins_1_timer.grid()
    bouton_seconde_moins_10_timer.grid()
    bouton_minute_timer.grid()
    bouton_minute_10_timer.grid()
    bouton_minute_moins_1_timer.grid()
    bouton_minute_moins_10_timer.grid()
    affichage_timer.grid()
    bouton_start_timer.grid()
    bouton_stop_timer.grid()
    bouton_restart_timer.grid()
    go()

def go_chrono():
    affichage_chrono.grid()
    bouton_start_chrono.grid()
    bouton_stop_chrono.grid()
    bouton_restart_chrono.grid()
    go()

def go_date_heure():
    affichage_date_heure.grid()
    go()
    update_affichage_date_heure()

def go_alarm():
    bouton_create_alarm.grid()
    go()
    affichage_alarm()
    alarm()

bouton_go_home = Button(text="Go Home",font=("arial",20),bg="#d67252", fg="black", command=go_home)
bouton_go_timer = Button(text="Go Timer",font=("arial",20),bg="#d67252", fg="black", command=go_timer)
bouton_go_chrono = Button(text="Go Chrono",font=("arial",20),bg="#d67252", fg="black", command=go_chrono)
bouton_go_date_heure = Button(text="Go Date et Heure",font=("arial",20),bg="#d67252", fg="black", command=go_date_heure)
bouton_go_alarm = Button(text="Go Alarm",font=("arial",20),bg="#d67252", fg="black", command=go_alarm)

bouton_go_home.grid(row=5, column=4)
bouton_go_timer.grid(row=3, column=4)
bouton_go_chrono.grid(row=7, column=4)
bouton_go_date_heure.grid(row=5, column=2)
bouton_go_alarm.grid(row=5, column=6, padx=50)



#timer

def update_affichage_timer():
    affichage_timer.config(text=f"TIMER : {hour_timer:02}:{minute_timer:02}:{seconde_timer:02}")

def choix_timer_seconde():
    global seconde_timer
    seconde_timer += 1
    time_sup_timer()
    time_inf_timer()
    update_affichage_timer()

def choix_timer_seconde_10():
    global seconde_timer
    seconde_timer += 10
    time_sup_timer()
    time_inf_timer()
    update_affichage_timer()

def choix_timer_minute():
    global minute_timer
    minute_timer += 1
    time_sup_timer()
    time_inf_timer()
    update_affichage_timer()

def choix_timer_minute_10():
    global minute_timer
    minute_timer += 10
    time_sup_timer()
    time_inf_timer()
    update_affichage_timer()

def choix_timer_seconde_moins_1():
    global seconde_timer
    seconde_timer -= 1
    time_sup_timer()
    time_inf_timer()
    update_affichage_timer()

def choix_timer_seconde_moins_10():
    global seconde_timer
    seconde_timer -= 10
    time_sup_timer()
    time_inf_timer()
    update_affichage_timer()

def choix_timer_minute_moins_1():
    global minute_timer
    minute_timer -= 1
    time_sup_timer()
    time_inf_timer()
    update_affichage_timer()

def choix_timer_minute_moins_10():
    global minute_timer
    minute_timer -= 10
    time_sup_timer()
    time_inf_timer()
    update_affichage_timer()

def time_sup_timer():
    global seconde_timer
    global minute_timer
    global hour_timer
    if seconde_timer >= 60:
        seconde_timer = 0
        minute_timer += 1
    if minute_timer >= 60:
        minute_timer = 0
        hour_timer += 1

def time_inf_timer():
    global seconde_timer
    global minute_timer
    global hour_timer
    if seconde_timer < 0:
        if minute_timer > 0:
            minute_timer -= 1
            seconde_timer += 60
        else:
            seconde_timer = 0
    if minute_timer < 0:
        if hour_timer > 0:
            hour_timer -= 1
            minute_timer += 60
        else:
            minute_timer = 0

def start_timer():
    global run_timer
    if not run_timer and (seconde_timer > 0 or minute_timer > 0 or hour_timer > 0):
        run_timer = True
        bouton_start_timer.config(state=DISABLED, bg="#313840")
        timer()

def timer():
    global seconde_timer
    global minute_timer
    global hour_timer
    global run_timer
    if run_timer:
        if seconde_timer != 0 or minute_timer != 0 or hour_timer != 0:
            if minute_timer == 0 and hour_timer > 0:
                hour_timer -= 1
                minute_timer += 60
            if seconde_timer == 0 and minute_timer > 0:
                minute_timer -= 1
                seconde_timer += 60
            seconde_timer -= 1
            window.after(1000, timer)
            update_affichage_timer()
        if seconde_timer == 0 and minute_timer == 0 and hour_timer == 0:
            update_affichage_timer()
            bouton_start_timer.config(state=NORMAL, bg="green")
            run_timer = False
            mixer.init()
            sound = mixer.Sound("alarm.mp3")
            sound.play()

def restart_timer():
    global seconde_timer
    global minute_timer
    global hour_timer
    seconde_timer = 0
    minute_timer = 0
    hour_timer = 0
    update_affichage_timer()

def stop_timer():
    global run_timer
    run_timer = False
    bouton_start_timer.config(state=NORMAL, bg="green")

bouton_seconde_timer = Button(text="+ 1 seconde au timer",font=("arial",20),bg="white", fg="black", command=choix_timer_seconde)
bouton_seconde_10_timer = Button(text="+ 10 seconde au timer",font=("arial",20),bg="white", fg="black", command=choix_timer_seconde_10)
bouton_minute_timer = Button(text="+ 1 minute au timer",font=("arial",20),bg="white", fg="black", command=choix_timer_minute)
bouton_minute_10_timer = Button(text="+ 10 minute au timer",font=("arial",20),bg="white", fg="black", command=choix_timer_minute_10)
bouton_seconde_moins_1_timer = Button(text="- 1 seconde au timer",font=("arial",20),bg="white", fg="black", command=choix_timer_seconde_moins_1)
bouton_seconde_moins_10_timer = Button(text="- 10 seconde au timer",font=("arial",20),bg="white", fg="black", command=choix_timer_seconde_moins_10)
bouton_minute_moins_1_timer = Button(text="- 1 minute au timer",font=("arial",20),bg="white", fg="black", command=choix_timer_minute_moins_1)
bouton_minute_moins_10_timer = Button(text="- 10 minute au timer",font=("arial",20),bg="white", fg="black", command=choix_timer_minute_moins_10)
bouton_start_timer = Button(text="START",font=("arial",20),bg="green", fg="black", command=start_timer)
bouton_restart_timer = Button(text="RESTART",font=("arial",20),bg="blue", fg="black", command=restart_timer)
bouton_stop_timer = Button(text="STOP",font=("arial",20),bg="red", fg="black", command=stop_timer)

affichage_timer = Label(text="TIMER : 00:00:00",font=("arial", 20),bg="#2e4053", fg="black")

bouton_seconde_timer.grid(row=2, column=2)
bouton_seconde_10_timer.grid(row=3, column=2)
bouton_seconde_moins_1_timer.grid(row=2, column=6)
bouton_seconde_moins_10_timer.grid(row=3, column=6)

bouton_minute_timer.grid(row=4, column=2)
bouton_minute_10_timer.grid(row=5, column=2)
bouton_minute_moins_1_timer.grid(row=4, column=6)
bouton_minute_moins_10_timer.grid(row=5, column=6)

affichage_timer.grid(row=1, column=4)
bouton_start_timer.grid(row=9, column=4)
bouton_stop_timer.grid(row=9, column=2)
bouton_restart_timer.grid(row=9, column=6)





#chrono

def update_affichage_chrono():
    affichage_chrono.config(text=f"CHRONOMETRE : {hour_chrono:02}:{minute_chrono:02}:{seconde_chrono:02}:{miliseconde_chrono:03}")

def start_chrono():
    global run_chrono
    if not run_chrono:
        run_chrono = True
        bouton_start_chrono.config(state=DISABLED, bg="#313840")
        chrono()

def stop_chrono():
    global run_chrono
    run_chrono = False
    bouton_start_chrono.config(state=NORMAL, bg="green")

def restart_chrono():
    global seconde_chrono, minute_chrono, hour_chrono, miliseconde_chrono, run_chrono
    run_chrono = False
    miliseconde_chrono = 0
    seconde_chrono = 0
    minute_chrono = 0
    hour_chrono = 0
    bouton_start_chrono.config(state=NORMAL, bg="green")
    update_affichage_chrono()

def chrono():
    global seconde_chrono, minute_chrono, hour_chrono, miliseconde_chrono
    if run_chrono:
        if miliseconde_chrono >= 1000:
            miliseconde_chrono = 0
            seconde_chrono += 1
        if seconde_chrono >= 60:
            minute_chrono += 1
            seconde_chrono = 0
        if minute_chrono >= 60:
            hour_chrono += 1
            minute_chrono = 0
        miliseconde_chrono += 1
        window.after(1, chrono)
        update_affichage_chrono()

bouton_start_chrono = Button(text="START",font=("arial",20),bg="green", fg="black", command=start_chrono)
bouton_stop_chrono = Button(text="STOP",font=("arial",20),bg="red", fg="black", command=stop_chrono)
bouton_restart_chrono = Button(text="RESTART",font=("arial",20),bg="blue", fg="black", command=restart_chrono)
affichage_chrono = Label(text="CHRONO : 00:00:00:000",font=("arial", 20),bg="#2e4053", fg="black")

affichage_chrono.grid(row=1, column=4)
bouton_start_chrono.grid(row=9, column=4)
bouton_stop_chrono.grid(row=9, column=2)
bouton_restart_chrono.grid(row=9, column=6)





#heure and date

def update_affichage_date_heure():
    global date_now, time_now
    date_now = datetime.today().strftime("%d-%m-%Y")
    time_now = datetime.today().strftime("%H:%M:%S")
    affichage_date_heure.config(text=f"DATE : {date_now}\nHEURE : {time_now}")
    window.after(1000, update_affichage_date_heure)

affichage_date_heure = Label(text=f"DATE : {date_now}\nHEURE : {time_now}",font=("arial", 20),bg="#2e4053", fg="black")

affichage_date_heure.grid(row=1, column=4)




#alarm


def update_affichage_create_alarm():
    affichage_create_alarm.config(text=f"ALARM : {hour_alarm:02}:{minute_alarm:02}")

def affichage_alarm():
    global minute_alarm, hour_alarm
    if alarm_counter >= 1:
        affichage_alarm0.grid()
        hour_alarm = 0
        minute_alarm = 0
    if alarm_counter >= 2:
        affichage_alarm1.grid()
        hour_alarm = 0
        minute_alarm = 0
    if alarm_counter >= 3:
        affichage_alarm2.grid()
        hour_alarm = 0
        minute_alarm = 0
    if alarm_counter >= 4:
        affichage_alarm3.grid()
        hour_alarm = 0
        minute_alarm = 0
    if alarm_counter >= 5:
        affichage_alarm4.grid()
        hour_alarm = 0
        minute_alarm = 0
    if alarm_counter >= 6:
        affichage_alarm5.grid()
        hour_alarm = 0
        minute_alarm = 0
    if alarm_counter >= 7:
        affichage_alarm6.grid()
        hour_alarm = 0
        minute_alarm = 0
        bouton_create_alarm.grid_remove()

def create_alarm():
    bouton_hour_alarm.grid()
    bouton_hour_10_alarm.grid()
    bouton_hour_moins_1_alarm.grid()
    bouton_hour_moins_10_alarm.grid()
    bouton_minute_alarm.grid()
    bouton_minute_10_alarm.grid()
    bouton_minute_moins_1_alarm.grid()
    bouton_minute_moins_10_alarm.grid()
    affichage_create_alarm.grid()
    bouton_confirm_create_alarm.grid()
    bouton_create_alarm.grid_remove()
    affichage_alarm0.grid_remove()
    affichage_alarm1.grid_remove()
    affichage_alarm2.grid_remove()
    affichage_alarm3.grid_remove()
    affichage_alarm4.grid_remove()
    affichage_alarm5.grid_remove()
    affichage_alarm6.grid_remove()

def confirm_create_alarm():
    global alarm_counter, minute_alarm, hour_alarm, time_alarm0, time_alarm1, time_alarm2, time_alarm3, time_alarm4, time_alarm5, time_alarm6
    alarm_counter += 1
    bouton_hour_alarm.grid_remove()
    bouton_hour_10_alarm.grid_remove()
    bouton_hour_moins_1_alarm.grid_remove()
    bouton_hour_moins_10_alarm.grid_remove()
    bouton_minute_alarm.grid_remove()
    bouton_minute_10_alarm.grid_remove()
    bouton_minute_moins_1_alarm.grid_remove()
    bouton_minute_moins_10_alarm.grid_remove()
    bouton_confirm_create_alarm.grid_remove()
    affichage_create_alarm.grid_remove()
    bouton_create_alarm.grid()
    affichage_alarm0.grid()
    bouton_create_alarm.grid()
    if alarm_counter == 1:
        affichage_alarm0.grid()
        affichage_alarm0.config(text=f"ALARM : {hour_alarm:02}:{minute_alarm:02}")
        time_alarm0 = datetime.now().replace(hour=hour_alarm, minute=minute_alarm, second=0, microsecond=0)
        hour_alarm = 0
        minute_alarm = 0
    if alarm_counter == 2:
        affichage_alarm1.grid()
        affichage_alarm1.config(text=f"ALARM : {hour_alarm:02}:{minute_alarm:02}")
        hour_alarm = 0
        minute_alarm = 0
    if alarm_counter == 3:
        affichage_alarm2.grid()
        affichage_alarm2.config(text=f"ALARM : {hour_alarm:02}:{minute_alarm:02}")
        hour_alarm = 0
        minute_alarm = 0
    if alarm_counter == 4:
        affichage_alarm3.grid()
        affichage_alarm3.config(text=f"ALARM : {hour_alarm:02}:{minute_alarm:02}")
        hour_alarm = 0
        minute_alarm = 0
    if alarm_counter == 5:
        affichage_alarm4.grid()
        affichage_alarm4.config(text=f"ALARM : {hour_alarm:02}:{minute_alarm:02}")
        hour_alarm = 0
        minute_alarm = 0
    if alarm_counter == 6:
        affichage_alarm5.grid()
        affichage_alarm5.config(text=f"ALARM : {hour_alarm:02}:{minute_alarm:02}")
        hour_alarm = 0
        minute_alarm = 0
    if alarm_counter >= 7:
        affichage_alarm6.grid()
        affichage_alarm6.config(text=f"ALARM : {hour_alarm:02}:{minute_alarm:02}")
        hour_alarm = 0
        minute_alarm = 0
        bouton_create_alarm.grid_remove()
    affichage_alarm()
    update_affichage_create_alarm()

def time_sup_alarm():
    global minute_alarm, hour_alarm
    if minute_alarm >= 60:
        minute_alarm = 0
        hour_alarm += 1
    if hour_alarm >= 24:
        hour_alarm = 0

def time_inf_alarm():
    global minute_alarm, hour_alarm
    if minute_alarm < 0:
        if hour_alarm > 0:
            hour_alarm -= 1
            minute_alarm += 60
        else:
            minute_alarm = 0
    if hour_alarm <= 0:
        hour_alarm = 0

def choix_alarm_hour():
    global hour_alarm
    hour_alarm += 1
    time_sup_alarm()
    time_inf_alarm()
    update_affichage_create_alarm()

def choix_alarm_hour_10():
    global hour_alarm
    hour_alarm += 10
    time_sup_alarm()
    time_inf_alarm()
    update_affichage_create_alarm()

def choix_alarm_minute():
    global minute_alarm
    minute_alarm += 1
    time_sup_alarm()
    time_inf_alarm()
    update_affichage_create_alarm()

def choix_alarm_minute_10():
    global minute_alarm
    minute_alarm += 10
    time_sup_alarm()
    time_inf_alarm()
    update_affichage_create_alarm()

def choix_alarm_hour_moins_1():
    global hour_alarm
    hour_alarm -= 1
    time_sup_alarm()
    time_inf_alarm()
    update_affichage_create_alarm()

def choix_alarm_hour_moins_10():
    global hour_alarm
    hour_alarm -= 10
    time_sup_alarm()
    time_inf_alarm()
    update_affichage_create_alarm()

def choix_alarm_minute_moins_1():
    global minute_alarm
    minute_alarm -= 1
    time_sup_alarm()
    time_inf_alarm()
    update_affichage_create_alarm()

def choix_alarm_minute_moins_10():
    global minute_alarm
    minute_alarm -= 10
    time_sup_alarm()
    time_inf_alarm()
    update_affichage_create_alarm()

def run_alarm_false():
    global run_alarm
    run_alarm = False

def alarm():
    global run_alarm
    time_now_alarm = datetime.now().replace(second=0,microsecond=0)
    if (time_now_alarm == time_alarm0 or time_now_alarm == time_alarm1 or time_now_alarm == time_alarm2 or time_now_alarm == time_alarm3 or time_now_alarm == time_alarm4 or time_now_alarm == time_alarm5 or time_now_alarm == time_alarm6) and not run_alarm:
        mixer.init()
        sound = mixer.Sound("alarm.mp3")
        sound.play()
        run_alarm = True
        window.after(60000, run_alarm_false)
    window.after(1000, alarm)


bouton_hour_alarm = Button(text="+ 1 hour au Alarm",font=("arial",20),bg="white", fg="black", command=choix_alarm_hour)
bouton_hour_10_alarm = Button(text="+ 10 hour au Alarm",font=("arial",20),bg="white", fg="black", command=choix_alarm_hour_10)
bouton_minute_alarm = Button(text="+ 1 minute au Alarm",font=("arial",20),bg="white", fg="black", command=choix_alarm_minute)
bouton_minute_10_alarm = Button(text="+ 10 minute au Alarm",font=("arial",20),bg="white", fg="black", command=choix_alarm_minute_10)
bouton_hour_moins_1_alarm = Button(text="- 1 hour au Alarm",font=("arial",20),bg="white", fg="black", command=choix_alarm_hour_moins_1)
bouton_hour_moins_10_alarm = Button(text="- 10 hour au Alarm",font=("arial",20),bg="white", fg="black", command=choix_alarm_hour_moins_10)
bouton_minute_moins_1_alarm = Button(text="- 1 minute au Alarm",font=("arial",20),bg="white", fg="black", command=choix_alarm_minute_moins_1)
bouton_minute_moins_10_alarm = Button(text="- 10 minute au Alarm",font=("arial",20),bg="white", fg="black", command=choix_alarm_minute_moins_10)
bouton_create_alarm = Button(text="CREATE",font=("arial",20),bg="green", fg="black", command=create_alarm)
bouton_confirm_create_alarm = Button(text="CREATE",font=("arial",20),bg="green", fg="black", command=confirm_create_alarm)

affichage_create_alarm = Label(text="ALARM : 00:00",font=("arial", 20),bg="#2e4053", fg="black")
affichage_alarm0 = Label(text="ALARM : 00:00",font=("arial", 20),bg="#2e4053", fg="black")
affichage_alarm1 = Label(text="ALARM : 00:00",font=("arial", 20),bg="#2e4053", fg="black")
affichage_alarm2 = Label(text="ALARM : 00:00",font=("arial", 20),bg="#2e4053", fg="black")
affichage_alarm3 = Label(text="ALARM : 00:00",font=("arial", 20),bg="#2e4053", fg="black")
affichage_alarm4 = Label(text="ALARM : 00:00",font=("arial", 20),bg="#2e4053", fg="black")
affichage_alarm5 = Label(text="ALARM : 00:00",font=("arial", 20),bg="#2e4053", fg="black")
affichage_alarm6 = Label(text="ALARM : 00:00",font=("arial", 20),bg="#2e4053", fg="black")

bouton_minute_alarm.grid(row=2, column=2)
bouton_minute_10_alarm.grid(row=3, column=2)
bouton_minute_moins_1_alarm.grid(row=2, column=6)
bouton_minute_moins_10_alarm.grid(row=3, column=6)

bouton_hour_alarm.grid(row=4, column=2)
bouton_hour_10_alarm.grid(row=5, column=2)
bouton_hour_moins_1_alarm.grid(row=4, column=6)
bouton_hour_moins_10_alarm.grid(row=5, column=6)

affichage_create_alarm.grid(row=1, column=4)
affichage_alarm0.grid(row=1, column=4)
affichage_alarm1.grid(row=2, column=4)
affichage_alarm2.grid(row=3, column=4)
affichage_alarm3.grid(row=4, column=4)
affichage_alarm4.grid(row=6, column=4)
affichage_alarm5.grid(row=7, column=4)
affichage_alarm6.grid(row=8, column=4)
bouton_create_alarm.grid(row=9, column=4)
bouton_confirm_create_alarm.grid(row=9, column=4)


go_home()

window.title("Horloge")
window.config(bg="#2e4053")

window.mainloop()