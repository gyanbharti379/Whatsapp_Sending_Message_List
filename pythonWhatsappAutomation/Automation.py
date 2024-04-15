import tkinter
import tkinter.messagebox
import tkinter.ttk
import pywhatkit
import datetime
import threading
import time
from DateTime import DateTime
from time import strftime


class Automation:
    def __init__(self):
        self.itemlist = []
        self.senditemlist = []
        self.mm = 1
        self.dt = DateTime()
        self.cont=0
        self.right_Frame_Title = "Summary of details:"

# ----------------------------Area for creating window -------------------END-------------------------#

        self.master = tkinter.Tk()
        self.master.title("Whatsapp Automatic Message Sending program")
        self.master.geometry("1300x710+300+50")

# ----------------------------Area for creating window -------------------END-------------------------#

# -------------------Area for widget to display on the window---------------------------------------------------------#

# ------------------Left Frame on the window----------------------------------------------------------#

        self.left_Frame = tkinter.Frame(self.master, bg="#004f9f", width=450, height=690)
        self.left_Frame.place(x=10, y=10)

        self.number_Label = tkinter.Label(self.left_Frame, bg="#004f9f",text="Phone Number:", fg="white",
                                          font=("bookman old style", 15))
        self.number_Label.place(x=10, y=10)

        self.pno_Entry = tkinter.Entry(self.left_Frame, bg="#004f9f",fg="#b6f9f5",font=("bookman old style", 15),width=26)
        self.pno_Entry.place(x=10, y=45)
        self.pno_Entry.focus_set()
        self.pno_Entry.bind("<Return>",self.onEnterPhoneNumberEntry)

        self.message_Left_Label = tkinter.Label(self.left_Frame, bg="#004f9f",text="Message:",fg="white",
                                                font=("bookman old style", 15))
        self.message_Left_Label.place(x=10, y=85)

        self.message_Left_TextArea= tkinter.Text(self.left_Frame,bg="#004f9f", fg="#b6f9f5",font=("bookman old style", 15), width=26, height=15)
        self.message_Left_TextArea.place(x=10, y=120)
        self.message_Left_TextArea.bind("<Return>", self.onEnterLeftTextArea)

        self.set_Timer_Label = tkinter.Label(self.left_Frame,text="Set Timer:",bg="#004f9f",fg="white",
                                             font=("bookman old style", 15))
        self.set_Timer_Label.place(x=10, y=570)

        self.hh_timer_spinner = tkinter.ttk.Spinbox(self.left_Frame, width=3,font=("bookman old style", 15), from_=1,to=12)
        self.hh_timer_spinner.place(x=150, y=570)
        self.hh_timer_spinner.bind("<Return>", self.onEnterHHTimerSpinner)

        self.mm_timer_spinner = tkinter.ttk.Spinbox(self.left_Frame, width=3, font=("bookman old style", 15),from_=0, to=59)
        self.mm_timer_spinner.place(x=250, y=570)
        self.mm_timer_spinner.bind("<Return>", self.onEnterMMTimerSpinner)

        self.ampm_timer_spinner = tkinter.ttk.Spinbox(self.left_Frame, width=3, font=("bookman old style", 15),values=["AM","PM"])
        self.ampm_timer_spinner.place(x=350, y=570)
        self.ampm_timer_spinner.bind("<Return>", self.onEnterAMPMTimerSpinner)

        self.save_btn = tkinter.Button(self.left_Frame, text="Save",font=("bookman old style", 15), bg="#004f9f", fg="white",
                                         width=12, height=1 )
        self.save_btn.place(x=10, y=620)
        self.save_btn.bind("<Return>",self.onEnterSaveButton)

        self.submit_btn = tkinter.Button(self.left_Frame, text="Send", font=("bookman old style", 15), bg="#004f9f",
                                         fg="white", command=self.OnClicksend,width=12, height=1)
        self.submit_btn.place(x=230, y=620)

# ------------------Left Frame on the window------------------------------END------------------------------------#

# ------------------Right Frame on the window--------------------------------------------------------------------#

        self.right_Frame = tkinter.Frame(self.master, bg="#66aae4",  width=830, height=690)
        self.right_Frame.place(x=460, y=10)

        self.message_right_Label = tkinter.Label(self.right_Frame,bg="#66aae4", text=self.right_Frame_Title, font=("bookman old style", 15))
        self.message_right_Label.place(x=200, y=10)

        self.message_right_TextArea = tkinter.Text(self.right_Frame, bg="#66aae4",font=("bookman old style", 15), width=50, height=22)
        self.message_right_TextArea.place(x=10, y=50)

# ------------------Right Frame on the window--------------------------------END--------------------------#

# --------------------------Time display in Spinner ------------------------------------------------------#

        self.timeDisplayInSpinner()

# -------------------------------------For clock Time ---------------------------------------------------#

        self.timeToDisplay()

        self.master.mainloop()

# -------------------Area for widget to display on the window-----------------------END-----------------#

# --------------------------Area for all Methods used in the requirements ---------------------------------#

# -----------Area for keyboard Entered function -----------------------------------------------------------#

    def onEnterPhoneNumberEntry(self,event):
        self.message_Left_TextArea.delete(1.0, tkinter.END)
        self.message_Left_TextArea.focus_set()

    def onEnterLeftTextArea(self,event):
        self.hh_timer_spinner.focus_set()
        self.hh_timer_spinner.delete(0,tkinter.END)

    def onEnterHHTimerSpinner(self,event):

        if self.hh_timer_spinner.get() == "":
            tkinter.messagebox.showerror("Error", "Enter Hour")
            self.hh_timer_spinner.focus_set()

        elif int(self.hh_timer_spinner.get()) >= 13:
            tkinter.messagebox.showerror("Error", "Value should be less than or equal to 12")
            self.hh_timer_spinner.focus_set()

        else:
            self.mm_timer_spinner.focus_set()
            self.mm_timer_spinner.delete(0, tkinter.END)


    def onEnterMMTimerSpinner(self, event):

        if self.mm_timer_spinner.get() == "":
            tkinter.messagebox.showerror("Error", "Enter Minute")
            self.mm_timer_spinner.focus_set()

        elif int(self.mm_timer_spinner.get()) >= 60:
            tkinter.messagebox.showerror("Error", "Value should be less than or equal to 59")
            self.mm_timer_spinner.focus_set()
        else:
            self.ampm_timer_spinner.focus_set()

    def onEnterAMPMTimerSpinner(self, event):
         self.save_btn.focus_set()


    def onEnterSaveButton(self,event):

        self.message_right_TextArea.delete(1.0, tkinter.END)

        hh = int(self.hh_timer_spinner.get())

        self.mm += int(self.mm_timer_spinner.get())

#------------change single digit number to two digit number ------------------#

        mm = "{:02d}".format(self.mm)
        AMPM = self.ampm_timer_spinner.get().upper()

#-----------Case for 1 hr 59 min -----------------------------------------------------------------#

        if self.mm == 60:
            hh += 1
            self.mm = 0

            if hh > 12:
                hh = 1

            time = f"{hh}:{mm} {AMPM}"

        else:
            time = f"{hh}:{mm} {AMPM}"

# ------------this condition convert 2 hr 00 min ------------------------------------------------- #

        s = "-"*12

        pn = f"Phone No: +91{self.pno_Entry.get()}{s}Sending Time: {time}\nMessage: "
        self.itemlist.append(pn)

        msg = self.message_Left_TextArea.get(1.0, tkinter.END)

        self.itemlist.append(msg)

        for item in self.itemlist:
            self.message_right_TextArea.insert(tkinter.END, item)

        if AMPM =="AM":

            if hh == 12:
                hh = 0
        else:
                hh += 12

        self.senditemlist.append(f"{self.pno_Entry.get()}-{msg}-{hh}-{mm}")
        self.mm = 1
        self.pno_Entry.focus_set()
        self.message_Left_TextArea.delete(1.0, tkinter.END)

# -----------Area for keyboard Entered function ----------------------------END-------------------------------#

# -----------------Mouse Click All Functions ----------------------------------------------------------------#
    def OnClicksend(self):

        count = 0

        maxi = len(self.senditemlist)

        while count < maxi:

            data = self.senditemlist[count].split("-")

            mm = "{:02d}".format(int(data[3].strip()))
            pre_time = f"{int(data[2].strip())}:{mm}:00"

            current_time = datetime.datetime.now().time()

            s = "-" * 40
            header = f"{s}\n\n"
            self.message_right_TextArea.insert(tkinter.END, header)
            display_message = f"({count + 1}). Message sending ...\n"
            self.message_right_TextArea.insert(tkinter.END, display_message)

            if pre_time > str(current_time):
                self.send(f"+91{data[0].strip()}", data[1].strip(), int(data[2].strip()), int(data[3].strip()),count + 1)

            count += 1

# -----------------Mouse Click All Functions ------------------------------END----------------------------------#

# ------------------Other Functions -----------------------------------------------------------------------------#

    def send(self, phone_no,message,hh,mm,count):

        try:

            pywhatkit.sendwhatmsg(phone_no,message,hh,mm)
            display_message = f"({count}). Message send successfully\n"
            self.message_right_TextArea.insert(tkinter.END, display_message)

        except Exception as e:
            print(str(e))

    def resetAllData(self):
        self.itemlist.clear()
        self.senditemlist.clear()
        self.pno_Entry.delete(0, tkinter.END)
        self.message_Left_TextArea.delete(1.0, tkinter.END)
        self.timeDisplayInSpinner()
        self.message_right_TextArea.delete(1.0, tkinter.END)
        self.pno_Entry.focus_set()

    def timeDisplayInSpinner(self):
        self.hh_timer_spinner.delete(0, tkinter.END)
        self.mm_timer_spinner.delete(0, tkinter.END)
        self.ampm_timer_spinner.delete(0, tkinter.END)

        self.hh_timer_spinner.insert(0, self.dt.h_12())
        self.mm_timer_spinner.insert(0, self.dt.minute())
        self.ampm_timer_spinner.insert(0, self.dt.ampm())

    def timeToDisplay(self):

# ----------------------------------Get current time---------------------------------------#

        current_time = strftime('%I:%M:%S %p')

#----------------------------- Update label text with current time ------------------------#

        s = self.right_Frame_Title + "     Time: "+ current_time
        self.message_right_Label.config(text=f"{s}")

#---------------------- Schedule the update_time function to run again after 1 second ------#

        self.message_right_Label.after(1000, self.timeToDisplay)

# -----------------other Functions --- -----------------------------------END -------------------------------------#

if __name__=="__main__":
    Automation()
