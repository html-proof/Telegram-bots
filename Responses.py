from datetime import datetime
import pyjokes

def sample_response(input_text):
    user_message =str(input_text).lower()

    if user_message in("hello","hai","hi","sup"):
        return "hello,welcome to FoxMan "
    if user_message in ("who are you?","who are you","name"):
        return "I AM Smart Robo"
    if user_message in ("time","What the time right now ?","date"):
        now =datetime.now()
        data_time =now.strftime("%d/%m/%y,%H:%M:%S")
        return str(data_time)
    if user_message in ("Good morning ","morning"):
        return "Good morning have wonderful day"
    if user_message in ("age","what is your age ?","what is your age ?"):
        return "I Have no age"
    if user_message in ("feel"):
        return "fine thanks"

    if user_message in ("jokes"):
        now =pyjokes.get_joke()
        return now
