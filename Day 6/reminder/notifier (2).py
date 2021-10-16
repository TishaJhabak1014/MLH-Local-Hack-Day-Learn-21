from plyer import notification
import time

def notifyMe(title, message= "It may be self-explanatory!"):
    notification.notify(
        title = title,
        message = message,
        app_icon =  "E:\\048-ToDoList\\assets\\notifier\Graphicloads-100-Flat-Clock.ico",#"E:\\048-ToDoList\\New folde\\Graphicloads-100-Flat-Clock.ico",  https://iconarchive.com/show/100-flat-icons-by-graphicloads/clock-icon.html
        timeout = 10,
    )
    
if __name__ == "__main__":
    # while True:
    #     notifyMe("Hey Fool!, take a break now!!", "Take some time to miss me.")
    #     time.sleep(6)
    title = input("What do you want to remaind urslf about?")
    message = input("You may provide some details...")
    min = float(input("In how many minutes do you want to notify urself?"))
    time.sleep(min*60)
    notifyMe(title, message)
    # notifyMe("Hey Fool!, take a break now!!", "Take some time to miss me.")