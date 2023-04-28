from tkinter import *
from chatbot import Chatbot
import re
import random
import json
from tkinter.filedialog import asksaveasfile

chat = Chatbot()

#####Chit-Chat###############
greet = ["hi", "hello", "hey", "helloo", "hellooo", "morning", "good day", "greetings", "greeting", "good to see you", "its good seeing you", "how are you", "how're you", "how are you doing", "how ya doin'", "how ya doin", "how is everything", "how is everything going", "how's everything going", "how is you", "how's you", "how are things", "how're things", "how is it going", "how's it going", "how's it goin'", "how's it goin", "how is life been treating you", "how's life been treating you", "how have you been", "how've you been", "what is up", "what's up", "what is cracking", "what's cracking", "what is good", 
             "what's good", 'all Good',"what is happening",'all well' ,"what's happening", "what is new", "what's new", 
             "what is neww", "g'day", "howdy",'yes', 'need some help','need help','what are you looking for',
             'how can i help', 'ask me anything','how are you','yeah','yup','i am good','how are you','good',
             "good afternoon", "good evening","g morining", "gmorning", "good morning"]


def get_response(text):
    if re.sub('[^a-z\']','',text.lower()) in greet:
        return random.choice(greet).capitalize()+'!!'
     
    return chat.help_bot(text)

BG_GRAY = '#ABB2B9'
BG_COLOR = '#17202A'
TEXT_COLOR = '#EAECEE'

FONT = 'Helvetica 14'
FONT_BOLD = 'Helvectica 13 bold'

class chatApplication:
    def __init__(self):
        self.window = Tk()
        self._setup_main_window()
        

    def run(self):
        self.window.mainloop()

    def _setup_main_window(self):
        self.window.title('Help Bot')
        self.window.resizable(width=True, height=True)
        self.window.configure(width=600,height=550,bg=BG_COLOR)

        # head label
        head_label = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR,
                           text='Ask me anything!!', font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)

        line = Label(self.window, width=450,bg=BG_GRAY)
        line.place(relwidth=1,rely=0.07, relheight=0.012)


        
        #text widget
        self.text_widget = Text(self.window, width=20,height=2, bg=BG_COLOR, font=('arial',16),
                                relief=RAISED,bd=3,fg=TEXT_COLOR,padx=5,pady=5,wrap=WORD)
        self.text_widget.place(relheight=0.745, relwidth=1,rely=0.08)                   
        self.text_widget.configure(cursor='arrow',state=DISABLED)

        #Scroll bar
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1,relx=0.9999)
        scrollbar.configure(command=self.text_widget.yview)

        # bottom label
        bottom_label = Label(self.window, bg=BG_GRAY, height=80)
        bottom_label.place(relwidth=1,rely=0.825)

        # message entry box
        self.msg_entry = Entry(bottom_label,bg="#2C3E50", fg=TEXT_COLOR, font=('arial',16))
        self.msg_entry.place(relwidth=0.74, relheight=0.06,rely=0.008, relx=0.011)
        self.msg_entry.bind('<Return>', self._on_enter_pressed)

        # send botton
        send_botton = Button(bottom_label, text='Ask',font=FONT_BOLD, width=20, bg=BG_GRAY,
                             command=lambda: self._on_enter_pressed(None))
        send_botton.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)


        

    def _on_enter_pressed(self,event):
        msg = self.msg_entry.get()
        self._insert_message(msg,'You')
    def _insert_message(self,msg,sender):
        if not msg:
            return
        self.msg_entry.delete(0,END)
        msg1 = f'{sender}: {msg}\n\n'
        self.save1 = msg1
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END,msg1)
        self.text_widget.configure(cursor='arrow',state=DISABLED)

        msg2 = f'Bot: {get_response(msg)}\n\n'
        self.save=msg2
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END,msg2)
        self.text_widget.configure(cursor='arrow',state=DISABLED)
        self.text_widget.see(END)

        # Saving the data in json 
        with open("user_data.json", "r") as f:  # reading a file
            data = json.load(f)

        
        data.append(self.save1[:-2])
        data.append(self.save[:-2])
        
        with open("user_data.json", "w") as f:
            json.dump(data, f,indent=4)
        



if __name__ == '__main__':
    app = chatApplication()
    app.run()