from tkinter import *
from tkinter import messagebox
import sqlite3 as sq
from datetime import *

root = Tk()
root.withdraw()

# ####################################---------tables---------##########################################


def tables():
    conn = sq.connect('records.db')
    c = conn.cursor()
    c.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name='FEE_RECORD';")
    table_check = c.fetchone()[0]
    if table_check == 0:
        c.execute('''CREATE TABLE STUDENTS_INFO1
                                 (REG                    INT      PRIMARY KEY,
                                 NAME                    TEXT,
                                 F_NAME                  TEXT,
                                 M_NAME                  TEXT,
                                 DOB                     CHAR,
                                 ADDRESS                 TEXT,
                                 PHONE_NO                INT,
                                 COURSE                  CHAR,
                                 BATCH_TIME              CHAR,
                                 NEXT_DUE                CHAR,
                                 ADMISSION_DATE          CHAR);''')
        #########################################################################################
        c.execute('''CREATE TABLE FEE_STRUCTURE10
                             (COURSE_NAME    CHAR      PRIMARY_KEY,
                              DURATION       CHAR,
                              REG00        CHAR,
                              INS01        CHAR,
                              INS02        CHAR,
                              INS03        CHAR,
                              INS04        CHAR,
                              INS05        CHAR,
                              INS06        CHAR,
                              INS07        CHAR,
                              INS08        CHAR,
                              INS09        CHAR,
                              INS010       CHAR,
                              INS011       CHAR,
                              INS012       CHAR,
                              INS013       CHAR,
                              INS014       CHAR,
                              INS015       CHAR,
                              INS016       CHAR,
                              INS017       CHAR,
                              INS018       CHAR);''')
        ###############################################################################################################
        c.execute('''CREATE TABLE FEE_RECORD
                                        (REG                     INT ,
                                         NAME                    TEXT,
                                         F_NAME                  TEXT,
                                         COURSE                  CHAR,
                                         INS                     CHAR,
                                         AMOUNT                  CHAR,
                                         DATE                    CHAR,
                                         TIME                    CHAR,
                                         SUBMITTED_BY            CHAR);''')
        ###############################################################################################################
        c.execute('''CREATE TABLE LOGIN_CRED
                                        (LOGIN_ID                CHAR,
                                         PASSWORD                CHAR);''')
        return True
    conn.commit()
    c.close()
    conn.close()


######################################################################################################


# ####################################------NEW_ADM---------##########################################

def new_adm():
    name_var = StringVar()
    fname_var = StringVar()
    mname_var = StringVar()
    dob_var = StringVar()
    add1_var = StringVar()
    add2_var = StringVar()
    add3_var = StringVar()
    pno_var = StringVar()

    def submit():
        name = name_var.get().upper()
        fname = fname_var.get().upper()
        mname = mname_var.get().upper()
        dob = dob_var.get()
        add = add1_var.get() + '@' + add2_var.get() + '@' + add3_var.get()
        phone_no = pno_var.get()
        course = course_var.get()
        batch_time = btime_var.get()
        dttime = datetime.now()
        date = str(dttime.date())
        if name == '':
            messagebox.showerror("Error", "Enter Student's Name")
        elif fname == '':
            messagebox.showerror("Error", "Enter Father's Name")
        elif mname == '':
            messagebox.showerror("Error", "Enter Mother's Name")
        elif dob == '' or dob == 'dd/mm/yyyy':
            messagebox.showerror("Error", "Enter DOB")
        elif phone_no == '':
            messagebox.showerror("Error", "Enter Contact No.")
        elif course == 'Select Course-':
            messagebox.showerror("Error", "Select Course")
        elif batch_time == 'Select Timing-':
            messagebox.showerror("Error", "Select Batch Time")
        else:
            ans = messagebox.askquestion("Are u sure", "Do You Want To Submit?")
            if ans == "yes":
                try:
                    c.execute('SELECT MAX(REG) FROM STUDENTS_INFO1')
                    reg = c.fetchone()[0] + 1
                except TypeError:
                    reg = 101

                command = "INSERT INTO STUDENTS_INFO1 \
                           VALUES (?,?,?,?,?,?,?,?,?,?,?)"
                data_tuple = (reg, name, fname, mname, dob, add, phone_no, course, batch_time, 'REG00', date)
                c.execute(command, data_tuple)
                conn.commit()
                c.close()
                conn.close()
                home.deiconify()
                sub1.destroy()
                messagebox.showinfo("Success", f"Admission Registered With Reg no. {reg}")

    def back():
        c.close()
        conn.close()
        sub1.destroy()
        home.deiconify()

    global sub1
    sub1 = Toplevel()
    sub1.geometry('900x650+200+20')
    sub1.title('New Admission')
    frame1 = LabelFrame(sub1, text="new admission", font=('San Fransisco', '15'))
    frame1.place(relx=0.1, rely=0.085, relwidth=0.8, relheight=0.85)
    conn = sq.connect('records.db')
    c = conn.cursor()
    lb2 = Label(sub1, text='Name-', font=('San Fransisco', 10))
    lb2.place(relx=0.35, rely=0.2)
    en2 = Entry(sub1, textvariable=name_var, font=('San Fransisco', '10'))
    en2.place(relx=0.46, rely=0.2, relwidth=0.18)
    lb3 = Label(sub1, text="Father's Name-", font=('San Fransisco', 10))
    lb3.place(relx=0.35, rely=0.25)
    en3 = Entry(sub1, textvariable=fname_var, font=('San Fransisco', '10'))
    en3.place(relx=0.46, rely=0.25, relwidth=0.18)
    lb4 = Label(sub1, text="Mother's Name-", font=('San Fransisco', 10))
    lb4.place(relx=0.35, rely=0.3)
    en4 = Entry(sub1, textvariable=mname_var, font=('San Fransisco', '10'))
    en4.place(relx=0.46, rely=0.3, relwidth=0.18)
    dob_var.set("dd/mm/yyyy")
    lb5 = Label(sub1, text='Date of Birth-', font=('San Fransisco', 10))
    lb5.place(relx=0.35, rely=0.35)
    en5 = Entry(sub1, textvariable=dob_var, font=('San Fransisco', '10'))
    en5.place(relx=0.46, rely=0.35, relwidth=0.18)
    lb6 = Label(sub1, text='Address-', font=('San Fransisco', 10))
    lb6.place(relx=0.35, rely=0.4)
    add1_var.set("line 1")
    en6 = Entry(sub1, textvariable=add1_var, font=('San Fransisco', '10'))
    en6.place(relx=0.46, rely=0.4, relwidth=0.18)
    add2_var.set("line 2")
    en7 = Entry(sub1, textvariable=add2_var, width=29, font=('San Fransisco', '10'))
    en7.place(relx=0.46, rely=0.45, relwidth=0.18)
    add3_var.set("line 3")
    en8 = Entry(sub1, textvariable=add3_var, width=29, font=('San Fransisco', '10'))
    en8.place(relx=0.46, rely=0.5, relwidth=0.18)
    lb7 = Label(sub1, text='Contact No.-', font=('San Fransisco', 10))
    lb7.place(relx=0.35, rely=0.55)
    en7 = Entry(sub1, textvariable=pno_var, width=29, font=('San Fransisco', '10'))
    en7.place(relx=0.46, rely=0.55, relwidth=0.18)
    lb8 = Label(sub1, text='Course-', font=('San Fransisco', 10))
    lb8.place(relx=0.35, rely=0.613)
    course_var = StringVar()
    c.execute("SELECT COURSE_NAME FROM FEE_STRUCTURE10;")
    courses = []
    r = c.fetchall()
    for i in r:
        courses.append(i[0])
    course_var.set('Select Course-')
    drop1 = OptionMenu(sub1, course_var, *courses)
    drop1.place(relx=0.455, rely=0.6, relwidth=0.18)
    lb9 = Label(sub1, text='Batch Timing-', font=('San Fransisco', 10))
    lb9.place(relx=0.35, rely=0.669)
    btime_var = StringVar()
    timings = ['07:00-08:00', '08:00-09:00', '09:00-10:00', '10:00-11:00', '11:00-12:00', '12:00-13:00', '13:00-14:00',
               '14:00-15:00', '15:00-16:00', '16:00-17:00', '17:00-18:00', '18:00-19:00', '19:00-20:00']
    btime_var.set('Select Timing-')
    drop2 = OptionMenu(sub1, btime_var, *timings)
    drop2.place(relx=0.455, rely=0.66, relwidth=0.18)
    bt4 = Button(sub1, command=submit, text='Submit', font=('San Fransisco', 10), fg="BLUE")
    bt4.place(relx=0.765, rely=0.85, relwidth=0.1)
    bt5 = Button(sub1, command=back, text='Back', font=('San Fransisco', 10))
    bt5.place(relx=0.135, rely=0.85, relwidth=0.1)
    home.withdraw()


#######################################################################################################


# ####################################------FEE_SUB---------###########################################

def fee_sub(admin):
    def next():
        reg_no = regno_var.get()
        name = name_var.get().upper()
        dob = dob_var.get()
        global selected_course
        selected_course = stud_courses_var.get()
        if reg_no == '' and name == '' and dob == '':
            messagebox.showerror('Error', ' Enter Student Details')
        elif reg_no == '':
            try:
                command = "SELECT * FROM STUDENTS_INFO1 WHERE NAME=? AND DOB=?"
                data_tuple = (name, dob)
                c.execute(command, data_tuple)
                global stud_details
                stud_details = c.fetchall()[0]
            except IndexError:
                messagebox.showerror("Error", "Name And DOB Did Not Match")
            else:
                existing_courses = stud_details[7].split(',')
                if selected_course in existing_courses:
                    fee_details()
                elif selected_course == "Select course-":
                    lb19 = Label(sub2, text='SELECT COURSE', font=('San Fransisco', '11'), fg="RED")
                    lb19.place(relx=0.44, rely=0.75)
                else:
                    lb20 = Label(sub2, text='SELECTED COURSE NOT FOUND', font=('San Fransisco', '11'), fg="RED")
                    lb20.place(relx=0.375, rely=0.7)
        else:
            try:
                command = "SELECT * FROM STUDENTS_INFO1 WHERE REG=?"
                data_tuple = (reg_no,)
                c.execute(command, data_tuple)
                stud_details = c.fetchall()[0]
            except IndexError:
                messagebox.showerror("Error", "Reg No. Not Found")
            else:
                existing_courses = stud_details[7].split(',')
                if selected_course in existing_courses:
                    fee_details()
                elif selected_course == "Select course-":
                    messagebox.showerror("Error", "Select Course")
                else:
                    messagebox.showerror("Error", "Selected Course Not Applicable")

    def fee_details():
        def fee_back():
            sub7.destroy()
            sub2.deiconify()

        sub2.withdraw()
        global sub7
        sub7 = Toplevel()
        sub7.geometry('900x650+200+20')
        sub7.title('Fee Submission')
        frame7 = LabelFrame(sub7, text='Fee Submission', font=('San Fransisco', '15'))
        frame7.place(relx=0.1, rely=0.085, relwidth=0.8, relheight=0.85)
        sub_frame = LabelFrame(sub7)
        sub_frame.place(relx=0.3, rely=0.2, relwidth=0.4, relheight=0.27)
        lb5 = Label(sub7, text='Reg No.-', font=('San Fransisco', '10'))
        lb5.place(relx=0.4, rely=0.25)
        lb6 = Label(sub7, text=stud_details[0], font=('San Fransisco', '10'))
        lb6.place(relx=0.52, rely=0.25)
        lb7 = Label(sub7, text='Name-', font=('San Fransisco', '10'))
        lb7.place(relx=0.4, rely=0.3)
        lb8 = Label(sub7, text=stud_details[1].lower().capitalize(), font=('San Fransisco', '10'))
        lb8.place(relx=0.52, rely=0.3)
        lb9 = Label(sub7, text="Father's Name-", font=('San Fransisco', '10'))
        lb9.place(relx=0.4, rely=0.35)
        lb10 = Label(sub7, text=stud_details[2].lower().capitalize(), font=('San Fransisco', '10'))
        lb10.place(relx=0.52, rely=0.35)
        lb11 = Label(sub7, text='Course-', font=('San Fransisco', '10'))
        lb11.place(relx=0.4, rely=0.4)
        lb12 = Label(sub7, text=selected_course, font=('San Fransisco', '10'))
        lb12.place(relx=0.52, rely=0.4)
        bt8 = Button(sub7, command=fee_back, text='Back', font=('San Fransisco', 10))
        bt8.place(relx=0.135, rely=0.85, relwidth=0.1)
        command = "SELECT * FROM FEE_STRUCTURE10 WHERE COURSE_NAME=?;"
        data_tuple = selected_course,
        c.execute(command, data_tuple)
        fee = c.fetchall()
        if stud_details[9] == 'FULLY PAID':
            lb18 = Label(sub7, text='TOTAL FEE ALREADY SUBMITTED', font=('San Fransisco', '12'))
            lb18.place(relx=0.35, rely=0.65)
            return ()
        else:
            existing_courses = stud_details[7].split(',')
            post = existing_courses.index(selected_course)
            existing_ins = stud_details[9].split(',')
            global nxtdue
            nxtdue = existing_ins[post]
            if nxtdue == 'FULLY PAID':
                lb18 = Label(sub7, text='TOTAL FEE ALREADY SUBMITTED', font=('San Fransisco', '12'))
                lb18.place(relx=0.35, rely=0.65)
                return ()
            elif nxtdue == 'REG00':
                command = "SELECT REG00 FROM FEE_STRUCTURE10 WHERE COURSE_NAME=?"
                data_tuple = selected_course,
                c.execute(command, data_tuple)
                global amount
                amount = c.fetchall()[0][0]
                global nxtdueup
                nxtdueup = 'INS01'
                if amount == '0':
                    command = "SELECT INS01 FROM FEE_STRUCTURE10 WHERE COURSE_NAME=?"
                    data_tuple = selected_course,
                    c.execute(command, data_tuple)
                    amount = c.fetchall()[0][0]
                    nxtdue = 'INS01'
                    nxtdueup = 'INS02'
            else:
                amount = fee[0][int(nxtdue[3:]) + 2]
                nxtamount = fee[0][int(nxtdue[3:]) + 3]
                if nxtamount == '0':
                    nxtdueup = 'FULLY PAID'
                elif int(nxtdue[3:5]) < 9:
                    nxtdueup = 'INS0' + str(int(nxtdue[3:5]) + 1)
                else:
                    nxtdueup = 'INS' + str(int(nxtdue[3:5]) + 1)
        lb14 = Label(sub7, text='Due Installment-', font=('San Fransisco', '10'))
        lb14.place(relx=0.4, rely=0.6)
        lb15 = Label(sub7, text=nxtdue, font=('San Fransisco', '10'))
        lb15.place(relx=0.52, rely=0.6)
        lb16 = Label(sub7, text='Amount-', font=('San Fransisco', '10'))
        lb16.place(relx=0.4, rely=0.65)
        amount_var.set(amount)
        en5 = Entry(sub7, textvariable=amount_var, font=('San Fransisco', '10'))
        en5.place(relx=0.52, rely=0.65, relwidth=0.1)
        bt5 = Button(sub7, command=submit, text='Submit', font=('San Fransisco', '10'))
        bt5.place(relx=0.765, rely=0.85, width=85)

    def submit():
        msg = messagebox.askquestion('Are u sure', 'Do you want to submit?')
        if msg == 'yes':
            final_amount = amount_var.get()
            dttime = datetime.now()
            fee_date = str(dttime.date())
            fee_time = str(dttime.time())[:8]
            existing_courses = stud_details[7].split(',')
            existing_ins = stud_details[9].split(',')
            post = existing_courses.index(selected_course)
            existing_ins[post] = nxtdueup
            for iii in existing_ins:
                if iii == "FULLY PAID":
                    continue
                else:
                    nxtdueupdate = ','.join(existing_ins)
                    break
            else:
                nxtdueupdate = "FULLY PAID"
            command = "UPDATE STUDENTS_INFO1 SET NEXT_DUE=? WHERE REG=?"
            data_tuple = (nxtdueupdate, stud_details[0])
            c.execute(command, data_tuple)
            command = "INSERT INTO FEE_RECORD \
                               VALUES (?,?,?,?,?,?,?,?,?)"
            data_tuple = (
             stud_details[0], stud_details[1], stud_details[2], selected_course, nxtdue, final_amount, fee_date
             , fee_time, admin)
            c.execute(command, data_tuple)
            conn.commit()
            sub2.deiconify()
            sub7.destroy()
            messagebox.showinfo("Success", "Fee Submitted Successfully")

    def back():
        c.close()
        conn.close()
        sub2.destroy()
        home.deiconify()

    global sub2
    sub2 = Toplevel()
    sub2.geometry('900x650+200+20')
    sub2.title('Fee Submission')
    frame2 = LabelFrame(sub2, text='Fee Submission', font=('San Fransisco', '15'))
    frame2.place(relx=0.1, rely=0.085, relwidth=0.8, relheight=0.85)
    conn = sq.connect('records.db')
    c = conn.cursor()
    regno_var = StringVar()
    name_var = StringVar()
    dob_var = StringVar()
    stud_courses_var = StringVar()
    amount_var = StringVar()
    lb1 = Label(sub2, text='Reg No.-', font=('San Fransisco', '10'))
    lb1.place(relx=0.35, rely=0.3)
    en1 = Entry(sub2, textvariable=regno_var, font=('San Fransisco', '10'))
    en1.place(relx=0.46, rely=0.3, relwidth=0.18)
    lb2 = Label(sub2, text='OR', font=('San Fransisco', '10'))
    lb2.place(relx=0.5, rely=0.35)
    lb3 = Label(sub2, text="Name-", font=('San Fransisco', '10'))
    lb3.place(relx=0.35, rely=0.4)
    en3 = Entry(sub2, textvariable=name_var, font=('San Fransisco', '10'))
    en3.place(relx=0.46, rely=0.4, relwidth=0.18)
    lb4 = Label(sub2, text="DOB-", font=('San Fransisco', '10'))
    lb4.place(relx=0.35, rely=0.45)
    en4 = Entry(sub2, textvariable=dob_var, font=('San Fransisco', '10'))
    en4.place(relx=0.46, rely=0.45, relwidth=0.18)
    c.execute("SELECT COURSE_NAME FROM FEE_STRUCTURE10;")
    all_courses = []
    r = c.fetchall()
    for i in r:
        all_courses.append(i[0])
    stud_courses_var.set('Select course-')
    lb13 = Label(sub2, text='Select Course-', font=('San Fransisco', '10'))
    lb13.place(relx=0.35, rely=0.55)
    drop1 = OptionMenu(sub2, stud_courses_var, *all_courses)
    drop1.place(relx=0.46, rely=0.541)
    bt6 = Button(sub2, command=next, text='Next', font=('San Fransisco', '10'))
    bt6.place(relx=0.765, rely=0.85, relwidth=0.1)
    bt7 = Button(sub2, command=back, text='Back', font=('San Fransisco', '10'))
    bt7.place(relx=0.135, rely=0.85, relwidth=0.1)
    home.withdraw()


###########################################################################################################


# ####################################------STUDENT_REC---------############################################

def student_rec():
    def student_record():
        def subback():
            sub4.destroy()
            sub3.deiconify()

        def delete():
            ans = messagebox.askquestion("Are u sure?", "Do you want to delete")
            if ans == "yes":
                command = "DELETE FROM STUDENTS_INFO1 WHERE REG=?;"
                data_tuple = stud_details[0],
                c.execute(command, data_tuple)
                conn.commit()
                c.close()
                conn.close()
                home.deiconify()
                messagebox.showinfo("Success", "Record Deleted Successfully")
                sub4.destroy()

        def edit():
            edname_var = StringVar()
            edfname_var = StringVar()
            edmname_var = StringVar()
            eddob_var = StringVar()
            edadd1_var = StringVar()
            edadd2_var = StringVar()
            edadd3_var = StringVar()
            edpno_var = StringVar()

            def subsubback31():
                subsub31.destroy()
                sub4.deiconify()

            def submit31():
                edname = edname_var.get().upper()
                edfname = edfname_var.get().upper()
                edmname = edmname_var.get().upper()
                eddob = eddob_var.get()
                edadd = edadd1_var.get() + '@' + edadd2_var.get() + '@' + edadd3_var.get()
                edphone_no = edpno_var.get()
                if edname == '':
                    messagebox.showerror("Error", "Student's Name can't be Empty")
                elif edfname == '':
                    messagebox.showerror("Error", "Father's Name can't be Empty")
                elif edmname == '':
                    messagebox.showerror("Error", "Mother's Name can't be Empty")
                elif eddob == '':
                    messagebox.showerror("Error", "DOB can't be Empty")
                elif edphone_no == '':
                    messagebox.showerror("Error", "Contact no. can't be Empty")
                else:
                    ans = messagebox.askquestion("Are u sure", "Do You Want To Submit?")
                    if ans == "yes":
                        command = "UPDATE STUDENTS_INFO1 SET NAME=?,F_NAME=?,M_NAME=?,DOB=?,ADDRESS=?,PHONE_NO=?" \
                                  "WHERE REG=?"
                        data_tuple = (edname, edfname, edmname, eddob, edadd, edphone_no, stud_details[0])
                        c.execute(command, data_tuple)
                        conn.commit()
                        sub3.deiconify()
                        messagebox.showinfo("Success", "Record Edited Successfully")
                        subsub31.destroy()

            global subsub31
            subsub31 = Toplevel()
            subsub31.geometry('900x650+200+20')
            subsub31.title('Student Details')
            subframe32 = LabelFrame(subsub31, text='Edit', font=('San Fransisco', '15'))
            subframe32.place(relx=0.1, rely=0.085, relwidth=0.8, relheight=0.85)
            lb23 = Label(subsub31, text='• Reg No.-', font=('San Fransisco', '10'))
            lb23.place(relx=0.35, rely=0.2)
            lb24 = Label(subsub31, text=stud_details[0], font=('San Fransisco', '10'))
            lb24.place(relx=0.5, rely=0.2)
            lb25 = Label(subsub31, text='• Name-', font=('San Fransisco', '10'))
            lb25.place(relx=0.35, rely=0.24)
            edname_var.set(stud_details[1])
            en5 = Entry(subsub31, textvariable=edname_var, font=('San Fransisco', '10'))
            en5.place(relx=0.5, rely=0.24, relwidth=0.18)
            lb26 = Label(subsub31, text="• Father's Name-", font=('San Fransisco', '10'))
            lb26.place(relx=0.35, rely=0.28)
            edfname_var.set(stud_details[2])
            en6 = Entry(subsub31, textvariable=edfname_var, font=('San Fransisco', '10'))
            en6.place(relx=0.5, rely=0.28, relwidth=0.18)
            lb27 = Label(subsub31, text="• Mother's Name-", font=('San Fransisco', '10'))
            lb27.place(relx=0.35, rely=0.32)
            edmname_var.set(stud_details[3])
            en7 = Entry(subsub31, textvariable=edmname_var, font=('San Fransisco', '10'))
            en7.place(relx=0.5, rely=0.32, relwidth=0.18)
            lb28 = Label(subsub31, text='• DOB-', font=('San Fransisco', '10'))
            lb28.place(relx=0.35, rely=0.36)
            eddob_var.set(stud_details[4])
            en8 = Entry(subsub31, textvariable=eddob_var, font=('San Fransisco', '10'))
            en8.place(relx=0.5, rely=0.36, relwidth=0.18)
            edaddressbyline = stud_details[5].split('@')
            lb29 = Label(subsub31, text='• Address-', font=('San Fransisco', '10'))
            lb29.place(relx=0.35, rely=0.4)
            edadd1_var.set(edaddressbyline[0])
            en9 = Entry(subsub31, textvariable=edadd1_var, font=('San Fransisco', '10'))
            en9.place(relx=0.5, rely=0.4, relwidth=0.18)
            edadd2_var.set(edaddressbyline[1])
            en10 = Entry(subsub31, textvariable=edadd2_var, font=('San Fransisco', '10'))
            en10.place(relx=0.5, rely=0.43, relwidth=0.18)
            edadd3_var.set(edaddressbyline[2])
            en11 = Entry(subsub31, textvariable=edadd3_var, font=('San Fransisco', '10'))
            en11.place(relx=0.5, rely=0.46, relwidth=0.18)
            lb30 = Label(subsub31, text='• Contact No.-', font=('San Fransisco', '10'))
            lb30.place(relx=0.35, rely=0.5)
            edpno_var.set(stud_details[6])
            en13 = Entry(subsub31, textvariable=edpno_var, font=('San Fransisco', '10'))
            en13.place(relx=0.5, rely=0.5, relwidth=0.18)
            lb31 = Label(subsub31, text='• Courses-', font=('San Fransisco', '10'))
            lb31.place(relx=0.35, rely=0.54)
            lb32 = Label(subsub31, text=stud_details[7], font=('San Fransisco', '10'))
            lb32.place(relx=0.5, rely=0.54)
            lb33 = Label(subsub31, text='• Batch Time-', font=('San Fransisco', '10'))
            lb33.place(relx=0.35, rely=0.58)
            lb42 = Label(subsub31, text=stud_details[8], font=('San Fransisco', '10'))
            lb42.place(relx=0.5, rely=0.58)
            lb34 = Label(subsub31, text='• Admission Date-', font=('San Fransisco', '10'))
            lb34.place(relx=0.35, rely=0.62)
            lb35 = Label(subsub31, text=stud_details[10], font=('San Fransisco', '10'))
            lb35.place(relx=0.5, rely=0.62)
            lb36 = Label(subsub31, text='• Due Installment-', font=('San Fransisco', '10'))
            lb36.place(relx=0.35, rely=0.66)
            lb37 = Label(subsub31, text=stud_details[9], font=('San Fransisco', '10'))
            lb37.place(relx=0.5, rely=0.66)
            bt12 = Button(subsub31, command=subsubback31, text='Back', font=('San Fransisco', '10'))
            bt12.place(relx=0.135, rely=0.85, relwidth=0.1)
            bt13 = Button(subsub31, command=submit31, text='Submit', font=('San Fransisco', '10'))
            bt13.place(relx=0.765, rely=0.85, relwidth=0.1)
            sub4.withdraw()

        def fee_details():
            def subsubsub3back():
                sub5.destroy()
                sub4.deiconify()

            def subsubsub3home():
                sub5.destroy()
                home.deiconify()

            global sub5
            sub5 = Toplevel()
            sub5.geometry('900x650+200+20')
            sub5.title('Student Details')
            subsubframe3 = LabelFrame(sub5, text='Fee Details', font=('San Fransisco', '15'))
            subsubframe3.place(relx=0.1, rely=0.085, relwidth=0.8, relheight=0.85)
            bt12 = Button(sub5, command=subsubsub3back, text='Back', font=('San Fransisco', '10'))
            bt12.place(relx=0.135, rely=0.85, relwidth=0.1)
            bt13 = Button(sub5, command=subsubsub3home, text='Home', font=('San Fransisco', '10'))
            bt13.place(relx=0.765, rely=0.85, relwidth=0.1)
            command = "SELECT * FROM FEE_RECORD WHERE REG=?"
            data_tuple = stud_details[0],
            c.execute(command, data_tuple)
            details = c.fetchall()
            scroll_bar = Scrollbar(sub5)
            scroll_bar.place(relx=0.865, rely=0.18, relheight=0.61, anchor="ne")
            my_list = Listbox(sub5, yscrollcommand=scroll_bar.set, font=('San Fransisco', '10'))
            for i in details:
                sentence = f"{i[3]} {i[4]} of {i[5]} submitted on {i[6]} at {i[7]} by {i[8]}"
                my_list.insert(END, sentence)
            my_list.place(relx=0.135, rely=0.18, relwidth=0.714, relheight=0.61)
            scroll_bar.config(command=my_list.yview)
            sub4.withdraw()

        global sub4
        sub4 = Toplevel()
        sub4.geometry('900x650+200+20')
        sub4.title('Student Details')
        subframe4 = LabelFrame(sub4, text='Student Details', font=('San Fransisco', '15'))
        subframe4.place(relx=0.1, rely=0.085, relwidth=0.8, relheight=0.85)
        lb5 = Label(sub4, text='• Reg No.-', font=('San Fransisco', '10'))
        lb5.place(relx=0.35, rely=0.2)
        lb6 = Label(sub4, text=stud_details[0], font=('San Fransisco', '10'))
        lb6.place(relx=0.5, rely=0.2)
        lb7 = Label(sub4, text='• Name-', font=('San Fransisco', '10'))
        lb7.place(relx=0.35, rely=0.24)
        lb8 = Label(sub4, text=stud_details[1].lower().capitalize(), font=('San Fransisco', '10'))
        lb8.place(relx=0.5, rely=0.24)
        lb9 = Label(sub4, text="• Father's Name-", font=('San Fransisco', '10'))
        lb9.place(relx=0.35, rely=0.28)
        lb10 = Label(sub4, text=stud_details[2].lower().capitalize(), font=('San Fransisco', '10'))
        lb10.place(relx=0.5, rely=0.28)
        lb11 = Label(sub4, text="• Mother's Name-", font=('San Fransisco', '10'))
        lb11.place(relx=0.35, rely=0.32)
        lb12 = Label(sub4, text=stud_details[3].lower().capitalize(), font=('San Fransisco', '10'))
        lb12.place(relx=0.5, rely=0.32)
        lb13 = Label(sub4, text='• DOB-', font=('San Fransisco', '10'))
        lb13.place(relx=0.35, rely=0.36)
        lb14 = Label(sub4, text=stud_details[4], font=('San Fransisco', '10'))
        lb14.place(relx=0.5, rely=0.36)
        addressbyline = stud_details[5].split('@')
        lb15 = Label(sub4, text='• Address-', font=('San Fransisco', '10'))
        lb15.place(relx=0.35, rely=0.4)
        lb16 = Label(sub4, text=addressbyline[0], font=('San Fransisco', '10'))
        lb16.place(relx=0.5, rely=0.4)
        lb17 = Label(sub4, text=addressbyline[1], font=('San Fransisco', '10'))
        lb17.place(relx=0.5, rely=0.43)
        lb18 = Label(sub4, text=addressbyline[2], font=('San Fransisco', '10'))
        lb18.place(relx=0.5, rely=0.46)
        lb19 = Label(sub4, text='• Contact No.-', font=('San Fransisco', '10'))
        lb19.place(relx=0.35, rely=0.5)
        lb20 = Label(sub4, text=stud_details[6], font=('San Fransisco', '10'))
        lb20.place(relx=0.5, rely=0.5)
        lb19 = Label(sub4, text='• Courses-', font=('San Fransisco', '10'))
        lb19.place(relx=0.35, rely=0.54)
        lb20 = Label(sub4, text=stud_details[7], font=('San Fransisco', '10'))
        lb20.place(relx=0.5, rely=0.54)
        lb19 = Label(sub4, text='• Batch Time-', font=('San Fransisco', '10'))
        lb19.place(relx=0.35, rely=0.58)
        lb20 = Label(sub4, text=stud_details[8], font=('San Fransisco', '10'))
        lb20.place(relx=0.5, rely=0.58)
        lb19 = Label(sub4, text='• Due Installment-', font=('San Fransisco', '10'))
        lb19.place(relx=0.35, rely=0.66)
        lb20 = Label(sub4, text=stud_details[9], font=('San Fransisco', '10'))
        lb20.place(relx=0.5, rely=0.66)
        lb21 = Label(sub4, text='• Admission Date-', font=('San Fransisco', '10'))
        lb21.place(relx=0.35, rely=0.62)
        lb22 = Label(sub4, text=stud_details[10], font=('San Fransisco', '10'))
        lb22.place(relx=0.5, rely=0.62)
        bt8 = Button(sub4, command=subback, text='Back', font=('San Fransisco', '10'))
        bt8.place(relx=0.135, rely=0.85, relwidth=0.1)
        bt9 = Button(sub4, command=fee_details, text='Fee Details', font=('San Fransisco', '10'))
        bt9.place(relx=0.765, rely=0.66, relwidth=0.1)
        bt10 = Button(sub4, command=delete, text='Delete', font=('San Fransisco', '10'), fg="RED")
        bt10.place(relx=0.765, rely=0.85, relwidth=0.1)
        bt11 = Button(sub4, command=edit, text='Edit', font=('San Fransisco', '10'))
        bt11.place(relx=0.45, rely=0.85, relwidth=0.1)
        sub3.withdraw()

    def next():
        reg_no = regno_var.get()
        name = name_var.get().upper()
        dob = dob_var.get()
        if reg_no == '' and name == '' and dob == '':
            messagebox.showerror('Error', ' Enter Student Details')
        elif reg_no == '':
            try:
                command = "SELECT * FROM STUDENTS_INFO1 WHERE NAME=? AND DOB=?"
                data_tuple = (name, dob)
                c.execute(command, data_tuple)
                global stud_details
                stud_details = c.fetchall()[0]
            except IndexError:
                messagebox.showerror("Error", "Name And DOB Did Not Match")
            else:
                student_record()
        else:
            try:
                command = "SELECT * FROM STUDENTS_INFO1 WHERE REG=?"
                data_tuple = (reg_no,)
                c.execute(command, data_tuple)
                stud_details = c.fetchall()[0]
            except IndexError:
                messagebox.showerror("Error", "Reg No. Not Found")
            else:
                student_record()

    def back():
        c.close()
        conn.close()
        sub3.destroy()
        home.deiconify()

    def all_records():
        def nexxt():
            def sub11_back():
                sub10.deiconify()
                sub11.destroy()

            def sub11_home():
                home.deiconify()
                sub10.destroy()
                sub11.destroy()

            global sub11
            sub11 = Toplevel()
            sub11.geometry('900x650+200+20')
            sub11.title('Student Record')
            frame11 = LabelFrame(sub11, text='All Records', font=('San Fransisco', '15'))
            frame11.place(relx=0.1, rely=0.085, relwidth=0.8, relheight=0.85)
            bt17 = Button(sub11, command=sub11_back, text='Back', font=('San Fransisco', '10'))
            bt17.place(relx=0.135, rely=0.85, relwidth=0.1)
            bt18 = Button(sub11, command=sub11_home, text='Home', font=('San Fransisco', '10'))
            bt18.place(relx=0.765, rely=0.85, relwidth=0.1)
            s_batch_time = batchtime_var.get()
            s_course = course_var.get()
            s_status = status_var.get()
            if s_batch_time == "All Batches" and s_course == "All Courses":
                c.execute("SELECT * FROM STUDENTS_INFO1")
            elif s_batch_time != "All Batches" and s_course == "All Courses":
                command = "SELECT * FROM STUDENTS_INFO1 WHERE BATCH_TIME=?"
                data_tuple = s_batch_time,
                c.execute(command, data_tuple)
            elif s_course != "All Courses" and s_batch_time == "All Batches":
                command = "SELECT * FROM STUDENTS_INFO1 WHERE COURSE=?"
                data_tuple = s_course,
                c.execute(command, data_tuple)
            else:
                command = "SELECT * FROM STUDENTS_INFO1 WHERE COURSE=? AND BATCH_TIME=?"
                data_tuple = s_course, s_batch_time
                c.execute(command, data_tuple)
            dttime = datetime.now()
            now_date = dttime.date()
            all_record = c.fetchall()
            scroll_bar = Scrollbar(sub11)
            scroll_bar.place(relx=0.865, rely=0.18, relheight=0.61, anchor="ne")
            my_list = Listbox(sub11, yscrollcommand=scroll_bar.set, font=('San Fransisco', '10'))
            total_students = 0
            for ii in all_record:
                student_courses = ii[7].split(',')
                admission_dates = ii[10].split(',')
                count = 0
                for k in student_courses:
                    student_course = k
                    command = "SELECT DURATION FROM FEE_STRUCTURE10 WHERE COURSE_NAME=?"
                    data_tupple = student_course,
                    c.execute(command, data_tupple)
                    data = c.fetchone()[0]
                    if s_status == "Current":
                        duration = int(data[:2])
                        admission_date = admission_dates[count]
                        count += 1
                        admission_year = int(admission_date[:4])
                        admission_month = int(admission_date[5:7])
                        admission_day = int(admission_date[8:])
                        end_day = admission_day + 1
                        end_month = admission_month + duration
                        end_year = admission_year
                        if end_month > 12:
                            end_year = admission_year + end_month // 12
                            end_month = end_month % 12
                        end_date = date(end_year, end_month, end_day)
                        if now_date < end_date:
                            sentence = f"{ii[0]}     {ii[1]}     {ii[2]}     {ii[7]}"
                            my_list.insert(END, sentence)
                            total_students += 1
                            break
                    else:
                        sentence = f"{ii[0]}     {ii[1]}     {ii[2]}     {ii[7]}"
                        my_list.insert(END, sentence)
                        total_students += 1
                        break
            if total_students == 0:
                sentence = " NO RECORD FOUND"
                my_list.insert(END, sentence)
            my_list.place(relx=0.135, rely=0.18, relwidth=0.714, relheight=0.61)
            scroll_bar.config(command=my_list.yview)
            lb41 = Label(sub11, text=f"Total Students = {total_students}", font=('San Fransisco', '12'))
            lb41.place(relx=0.425, rely=0.85)
            sub10.withdraw()

        def all_records_back():
            sub10.destroy()
            sub3.deiconify()

        global sub10
        sub10 = Toplevel()
        sub10.geometry('900x650+200+20')
        sub10.title('Student Record')
        frame10 = LabelFrame(sub10, text='All Records', font=('San Fransisco', '15'))
        frame10.place(relx=0.1, rely=0.085, relwidth=0.8, relheight=0.85)
        lb38 = Label(sub10, text='Batch Timing-', font=('San Fransisco', '10'))
        lb38.place(relx=0.36, rely=0.349)
        batchtime_var = StringVar()
        batchtime_var.set("All Batches")
        all_batch_times = ['07:00-08:00', '08:00-09:00', '09:00-10:00', '10:00-11:00', '11:00-12:00', '12:00-13:00',
                           '13:00-14:00', '14:00-15:00', '15:00-16:00', '16:00-17:00', '17:00-18:00', '18:00-19:00',
                           '19:00-20:00', 'All Batches']
        drop1 = OptionMenu(sub10, batchtime_var, *all_batch_times)
        drop1.place(relx=0.47, rely=0.34, relwidth=0.15)
        lb39 = Label(sub10, text="Course-", font=('San Fransisco', '10'))
        lb39.place(relx=0.36, rely=0.429)
        c.execute("SELECT COURSE_NAME FROM FEE_STRUCTURE10;")
        courses = []
        r = c.fetchall()
        for i in r:
            courses.append(i[0])
        courses.append("All Courses")
        course_var = StringVar()
        course_var.set("All Courses")
        drop2 = OptionMenu(sub10, course_var, *courses)
        drop2.place(relx=0.47, rely=0.42, relwidth=0.15)
        lb40 = Label(sub10, text="Status-", font=('San Fransisco', '10'))
        lb40.place(relx=0.36, rely=0.509)
        status_var = StringVar()
        status_var.set("Current")
        options = ["Current", "All"]
        drop3 = OptionMenu(sub10, status_var, *options)
        drop3.place(relx=0.47, rely=0.5, relwidth=0.15)
        bt15 = Button(sub10, command=nexxt, text='Next', font=('San Fransisco', '10'))
        bt15.place(relx=0.765, rely=0.85, relwidth=0.1)
        bt16 = Button(sub10, command=all_records_back, text='Back', font=('San Fransisco', '10'))
        bt16.place(relx=0.135, rely=0.85, relwidth=0.1)
        sub3.withdraw()

    global sub3
    sub3 = Toplevel()
    sub3.geometry('900x650+200+20')
    sub3.title('Student Record')
    conn = sq.connect('records.db')
    c = conn.cursor()
    regno_var = StringVar()
    name_var = StringVar()
    dob_var = StringVar()
    frame3 = LabelFrame(sub3, text='Student Record', font=('San Fransisco', '15'))
    frame3.place(relx=0.1, rely=0.085, relwidth=0.8, relheight=0.85)
    lb1 = Label(sub3, text='Reg No.-', font=('San Fransisco', '10'))
    lb1.place(relx=0.35, rely=0.33)
    en1 = Entry(sub3, textvariable=regno_var, font=('San Fransisco', '10'))
    en1.place(relx=0.46, rely=0.33, relwidth=0.18)
    lb2 = Label(sub3, text='OR', font=('San Fransisco', '10'))
    lb2.place(relx=0.5, rely=0.38)
    lb3 = Label(sub3, text="Name-", font=('San Fransisco', '10'))
    lb3.place(relx=0.35, rely=0.43)
    en3 = Entry(sub3, textvariable=name_var, font=('San Fransisco', '10'))
    en3.place(relx=0.46, rely=0.43, relwidth=0.18)
    lb4 = Label(sub3, text="DOB-", font=('San Fransisco', '10'))
    lb4.place(relx=0.35, rely=0.48)
    en4 = Entry(sub3, textvariable=dob_var, font=('San Fransisco', '10'))
    en4.place(relx=0.46, rely=0.484, relwidth=0.18)
    bt6 = Button(sub3, command=next, text='Next', font=('San Fransisco', '10'))
    bt6.place(relx=0.765, rely=0.85, relwidth=0.1)
    bt7 = Button(sub3, command=back, text='Back', font=('San Fransisco', '10'))
    bt7.place(relx=0.135, rely=0.85, relwidth=0.1)
    bt14 = Button(sub3, command=all_records, text='All Records', font=('San Fransisco', '10'))
    bt14.place(relx=0.45, rely=0.85, relwidth=0.1)
    home.withdraw()


########################################################################################################


# ####################################------ADD_COURSE-------############################################

def add_course():
    def disstudent_details():
        def subsub6back():
            subsub6.destroy()
            sub6.deiconify()

        global subsub6
        subsub6 = Toplevel()
        subsub6.geometry('900x650+200+20')
        subsub6.title('Add Course')
        subframe6 = LabelFrame(subsub6, text='Add Course', font=('San Fransisco', '15'))
        subframe6.place(relx=0.1, rely=0.085, relwidth=0.8, relheight=0.85)
        sub_sub_frame = LabelFrame(subsub6)
        sub_sub_frame.place(relx=0.3, rely=0.2, relwidth=0.4, relheight=0.27)
        lb5 = Label(subsub6, text='Reg No.-', font=('San Fransisco', '10'))
        lb5.place(relx=0.4, rely=0.25)
        lb6 = Label(subsub6, text=stud_details[0], font=('San Fransisco', '10'))
        lb6.place(relx=0.52, rely=0.25)
        lb7 = Label(subsub6, text='Name-', font=('San Fransisco', '10'))
        lb7.place(relx=0.4, rely=0.3)
        lb8 = Label(subsub6, text=stud_details[1].lower().capitalize(), font=('San Fransisco', '10'))
        lb8.place(relx=0.52, rely=0.3)
        lb9 = Label(subsub6, text="Father's Name-", font=('San Fransisco', '10'))
        lb9.place(relx=0.4, rely=0.35)
        lb10 = Label(subsub6, text=stud_details[2].lower().capitalize(), font=('San Fransisco', '10'))
        lb10.place(relx=0.52, rely=0.35)
        lb11 = Label(subsub6, text='Course(s)-', font=('San Fransisco', '10'))
        lb11.place(relx=0.4, rely=0.4)
        lb12 = Label(subsub6, text=stud_details[7], font=('San Fransisco', '10'))
        lb12.place(relx=0.52, rely=0.4)
        bt8 = Button(subsub6, command=subsub6back, text='Back', font=('San Fransisco', '10'))
        bt8.place(relx=0.135, rely=0.85, width=85)
        c.execute("SELECT COURSE_NAME FROM FEE_STRUCTURE10;")
        courses = []
        r = c.fetchall()
        for i in r:
            if i[0] not in stud_details[7]:
                courses.append(i[0])
        if not courses:
            lb13 = Label(subsub6, text='NO COURSE TO ADD', font=('San Fransisco', '13'), fg='RED')
            lb13.place(relx=0.42, rely=0.6)
        else:
            stud_courses_var.set('Select course-')
            lb13 = Label(subsub6, text='Course-', font=('San Fransisco', '10'))
            lb13.place(relx=0.37, rely=0.6)
            drop1 = OptionMenu(subsub6, stud_courses_var, *courses)
            drop1.place(relx=0.49, rely=0.594)
            lb14 = Label(subsub6, text='Batch Time-', font=('San Fransisco', '10'), fg="")
            lb14.place(relx=0.37, rely=0.65)
            timings = ['07:00-08:00', '08:00-09:00', '09:00-10:00', '10:00-11:00', '11:00-12:00', '12:00-13:00',
                       '13:00-14:00', '14:00-15:00', '15:00-16:00', '16:00-17:00', '17:00-18:00', '18:00-19:00',
                       '19:00-20:00']
            btime_var.set('Select timing-')
            drop2 = OptionMenu(subsub6, btime_var, *timings)
            drop2.place(relx=0.49, rely=0.644)
            bt5 = Button(subsub6, command=submit, text='Submit', font=('San Fransisco', '10'))
            bt5.place(relx=0.765, rely=0.85, width=85)
        sub6.withdraw()

    def submit():
        new_course = stud_courses_var.get()
        new_time = btime_var.get()
        if new_course == "Select course-":
            messagebox.showerror("Error", "Select Course To Add")
        elif new_time == "Select timing-":
            messagebox.showerror("Error", "Select Batch Time")
        else:
            ans = messagebox.askquestion("Are u sure", "Do You Want To Submit?")
            if ans == "yes":
                upcourses = stud_details[7] + ',' + new_course
                upins = stud_details[9] + ',' + 'REG00'
                dttime = datetime.now()
                date_now = str(dttime.date())
                updoa = stud_details[10] + ',' + date_now
                uptime = stud_details[8] + ',' + new_time
                command = "UPDATE STUDENTS_INFO1 SET COURSE=?,NEXT_DUE=?,ADMISSION_DATE=?,BATCH_TIME=? WHERE REG=?"
                data_tuple = upcourses, upins, updoa, uptime, stud_details[0]
                c.execute(command, data_tuple)
                conn.commit()
                sub6.deiconify()
                messagebox.showinfo("Success", "Course Added Successfully.")
                subsub6.destroy()

    def next():
        reg_no = regno_var.get()
        name = name_var.get().upper()
        dob = dob_var.get()
        if reg_no == '' and name == '' and dob == '':
            messagebox.showerror('Error', ' Enter Student Details')
        elif reg_no == '':
            try:
                command = "SELECT * FROM STUDENTS_INFO1 WHERE NAME=? AND DOB=?"
                data_tuple = (name, dob)
                c.execute(command, data_tuple)
                global stud_details
                stud_details = c.fetchall()[0]
            except IndexError:
                messagebox.showerror("Error", "Name And DOB Did Not Match")
            else:
                disstudent_details()
        else:
            try:
                command = "SELECT * FROM STUDENTS_INFO1 WHERE REG=?"
                data_tuple = (reg_no,)
                c.execute(command, data_tuple)
                stud_details = c.fetchall()[0]
            except IndexError:
                messagebox.showerror("Error", "Reg No. Not Found")
            else:
                disstudent_details()

    def back():
        c.close()
        conn.close()
        sub6.destroy()
        home.deiconify()

    global sub6
    sub6 = Toplevel()
    sub6.geometry('900x650+200+20')
    sub6.title('Add Course')
    conn = sq.connect('records.db')
    c = conn.cursor()
    regno_var = StringVar()
    name_var = StringVar()
    dob_var = StringVar()
    stud_courses_var = StringVar()
    btime_var = StringVar()
    hd = Label(sub6, text='Add Course:-', font=('San Fransisco', '15'))
    hd.place(relx=0.35, rely=0.13)
    frame6 = LabelFrame(sub6, text='Add Course', font=('San Fransisco', '15'))
    frame6.place(relx=0.1, rely=0.085, relwidth=0.8, relheight=0.85)
    lb1 = Label(sub6, text='Reg No.-', font=('San Fransisco', '10'))
    lb1.place(relx=0.35, rely=0.33)
    en1 = Entry(sub6, textvariable=regno_var, font=('San Fransisco', '10'))
    en1.place(relx=0.46, rely=0.33, relwidth=0.18)
    lb2 = Label(sub6, text='OR', font=('San Fransisco', '10'))
    lb2.place(relx=0.5, rely=0.38)
    lb3 = Label(sub6, text="Name-", font=('San Fransisco', '10'))
    lb3.place(relx=0.35, rely=0.43)
    en3 = Entry(sub6, textvariable=name_var, font=('San Fransisco', '10'))
    en3.place(relx=0.46, rely=0.43, relwidth=0.18)
    lb4 = Label(sub6, text="DOB-", font=('San Fransisco', '10'))
    lb4.place(relx=0.35, rely=0.48)
    en4 = Entry(sub6, textvariable=dob_var, font=('San Fransisco', '10'))
    en4.place(relx=0.46, rely=0.48, relwidth=0.18)
    bt6 = Button(sub6, command=next, text='Next', font=('San Fransisco', '10'))
    bt6.place(relx=0.765, rely=0.85, width=85)
    bt7 = Button(sub6, command=back, text='Back', font=('San Fransisco', '10'))
    bt7.place(relx=0.135, rely=0.85, width=85)
    home.withdraw()


#######################################################################################################


# ####################################------PENDING_FEE-----###########################################

def pending_fee():
    def nexxt():
        def sub12_back():
            sub8.deiconify()
            sub12.destroy()

        def sub12_home():
            c.close()
            conn.close()
            home.deiconify()
            sub8.destroy()
            sub12.destroy()

        global sub12
        sub12 = Toplevel()
        sub12.geometry('900x650+200+20')
        sub12.title('Pending Fee')
        frame12 = LabelFrame(sub12, text='Pending', font=('San Fransisco', '15'))
        frame12.place(relx=0.1, rely=0.085, relwidth=0.8, relheight=0.85)
        bt3 = Button(sub12, command=sub12_back, text='Back', font=('San Fransisco', '10'))
        bt3.place(relx=0.135, rely=0.85, relwidth=0.1)
        bt4 = Button(sub12, command=sub12_home, text='Home', font=('San Fransisco', '10'))
        bt4.place(relx=0.765, rely=0.85, relwidth=0.1)
        s_batch_time = batchtime_var.get()
        s_course = course_var.get()
        if s_batch_time == "All Batches" and s_course == "All Courses":
            c.execute('SELECT * FROM STUDENTS_INFO1 WHERE NEXT_DUE!="FULLY PAID"')
        elif s_batch_time != "All Batches" and s_course == "All Courses":
            command = "SELECT * FROM STUDENTS_INFO1 WHERE BATCH_TIME=? AND NEXT_DUE!='FULLY PAID'"
            data_tuple = s_batch_time,
            c.execute(command, data_tuple)
        elif s_course != "All Courses" and s_batch_time == "All Batches":
            command = "SELECT * FROM STUDENTS_INFO1 WHERE COURSE=? AND NEXT_DUE!='FULLY PAID'"
            data_tuple = s_course,
            c.execute(command, data_tuple)
        else:
            command = "SELECT * FROM STUDENTS_INFO1 WHERE COURSE=? AND BATCH_TIME=? AND NEXT_DUE!='FULLY PAID'"
            data_tuple = s_course, s_batch_time
            c.execute(command, data_tuple)
        student_details = c.fetchall()
        dttime = datetime.now()
        now_date = dttime.date()
        scroll_bar = Scrollbar(sub12)
        scroll_bar.place(relx=0.865, rely=0.18, relheight=0.61, anchor="ne")
        my_list = Listbox(sub12, yscrollcommand=scroll_bar.set, font=('San Fransisco', '10'))
        pending_fee_no = 0
        for ii in student_details:
            reg_no = ii[0]
            name = ii[1]
            student_course = ii[7].split(',')
            next_dues = ii[9].split(',')
            admission_dates = ii[10].split(',')
            count = 0
            for k in student_course:
                next_due = next_dues[count]
                if next_due == "FULLY PAID":
                    continue
                admission_date = admission_dates[count]
                count += 1
                admission_year = int(admission_date[:4])
                admission_month = int(admission_date[5:7])
                admission_day = int(admission_date[8:])
                due_day = admission_day
                if next_due == 'REG00':
                    due_month = admission_month
                else:
                    due_month = admission_month + int(next_due[3:]) - 1
                due_year = admission_year
                if due_month > 12:
                    due_year = admission_year + due_month // 12
                    due_month = due_month % 12
                command = "SELECT REG00 FROM FEE_STRUCTURE10 WHERE COURSE_NAME=?"
                data_tuple = k,
                c.execute(command, data_tuple)
                fee_amount = c.fetchone()[0]
                if fee_amount == "0":
                    next_due = "INS01"
                due_date = date(due_year, due_month, due_day)
                if due_date <= now_date:
                    sentence = f" {next_due}   Due   of   {name}({reg_no})   from   {due_date}   in   {k} "
                    my_list.insert(END, sentence)
                    pending_fee_no += 1
        if pending_fee_no == 0:
            my_list.insert(END, "NO FEE PENDING.")
        lb3 = Label(sub12, text=f"{pending_fee_no}  Fee Pending", font=('San Fransisco', '12'), fg="RED")
        lb3.place(relx=0.435, rely=0.85)
        my_list.place(relx=0.135, rely=0.17, relwidth=0.714, relheight=0.61)
        scroll_bar.config(command=my_list.yview)
        sub8.withdraw()

    def sub8_back():
        home.deiconify()
        sub8.destroy()
        c.close()
        conn.close()

    conn = sq.connect('records.db')
    c = conn.cursor()
    global sub8
    sub8 = Toplevel()
    sub8.geometry('900x650+200+20')
    sub8.title('Pending Fee')
    frame8 = LabelFrame(sub8, text='Pending Fee', font=('San Fransisco', '15'))
    frame8.place(relx=0.1, rely=0.085, relwidth=0.8, relheight=0.85)
    bt1 = Button(sub8, command=sub8_back, text='Back', font=('San Fransisco', '10'))
    bt1.place(relx=0.135, rely=0.85, relwidth=0.1)
    bt2 = Button(sub8, command=nexxt, text='Next', font=('San Fransisco', '10'))
    bt2.place(relx=0.765, rely=0.85, width=85)
    lb1 = Label(sub8, text='Batch Timing-', font=('San Fransisco', '10'))
    lb1.place(relx=0.36, rely=0.409)
    batchtime_var = StringVar()
    batchtime_var.set("All Batches")
    all_batch_times = ['07:00-08:00', '08:00-09:00', '09:00-10:00', '10:00-11:00', '11:00-12:00', '12:00-13:00',
                       '13:00-14:00', '14:00-15:00', '15:00-16:00', '16:00-17:00', '17:00-18:00', '18:00-19:00',
                       '19:00-20:00', 'All Batches']
    drop1 = OptionMenu(sub8, batchtime_var, *all_batch_times)
    drop1.place(relx=0.47, rely=0.4, relwidth=0.15)
    lb2 = Label(sub8, text="Course-", font=('San Fransisco', '10'))
    lb2.place(relx=0.36, rely=0.489)
    c.execute("SELECT COURSE_NAME FROM FEE_STRUCTURE10;")
    courses = []
    r = c.fetchall()
    for i in r:
        courses.append(i[0])
    courses.append("All Courses")
    course_var = StringVar()
    course_var.set("All Courses")
    drop2 = OptionMenu(sub8, course_var, *courses)
    drop2.place(relx=0.47, rely=0.48, relwidth=0.15)
    home.withdraw()


######################################################################################################


# ####################################------FEE_RECORD------###########################################

def fee_record(admin):
    def back():
        home.deiconify()
        sub9.destroy()
        c.close()
        conn.close()

    def next():
        from_date = from_var.get()
        to_date = to_var.get()
        try:
            from_day = int(from_date[:2])
            from_month = int(from_date[3:5])
            from_year = int(from_date[6:])
            from_date = date(from_year, from_month, from_day)
            to_day = int(to_date[:2])
            to_month = int(to_date[3:5])
            to_year = int(to_date[6:])
            to_date = date(to_year, to_month, to_day)
        except ValueError:
            messagebox.showerror("Error", "Invalid Date")
        else:
            dttime = datetime.now()
            now_date = dttime.date()
            if from_date > to_date or to_date > now_date:
                messagebox.showerror("Error", "Invalid Date")
            else:
                display_fee_records(from_date, to_date)

    def display_fee_records(start_date, end_date):
        def back_fee_record():
            sub9.deiconify()
            sub10.destroy()

        def home_sub10():
            home.deiconify()
            c.close()
            conn.close()
            sub9.destroy()
            sub10.destroy()

        global sub10
        sub10 = Toplevel()
        sub10.geometry('900x650+200+20')
        sub10.title('Fee Record')
        frame9 = LabelFrame(sub10, text='Fee Record', font=('San Fransisco', '15'))
        frame9.place(relx=0.1, rely=0.085, relwidth=0.8, relheight=0.85)
        bt3 = Button(sub10, command=back_fee_record, text='Back', font=('San Fransisco', '10'))
        bt3.place(relx=0.135, rely=0.85, relwidth=0.1)
        bt4 = Button(sub10, command=home_sub10, text='Home', font=('San Fransisco', '10'))
        bt4.place(relx=0.765, rely=0.85, relwidth=0.1)
        delta = timedelta(days=1)
        submitted_by = submitted_by_var.get()
        fee_amount = 0
        fee_no = 0
        scroll_bar = Scrollbar(sub10)
        scroll_bar.place(relx=0.865, rely=0.18, relheight=0.61, anchor="ne")
        my_list = Listbox(sub10, yscrollcommand=scroll_bar.set, font=('San Fransisco', '10'))
        while start_date <= end_date:
            if submitted_by == 'All':
                command = "SELECT * FROM FEE_RECORD WHERE DATE=?"
                data_tuple = str(start_date),
            else:
                command = "SELECT * FROM FEE_RECORD WHERE DATE=? AND SUBMITTED_BY=? "
                data_tuple = str(start_date), admin
            c.execute(command, data_tuple)
            record = c.fetchall()
            for i in record:
                sentence = f"{i[4]}({i[5]})  of  {i[1]}({i[0]})  Submitted  by  {i[8]}  on  {i[6]}"
                my_list.insert(END, sentence)
                fee_amount += int(i[5])
                fee_no += 1
            start_date += delta
        if fee_no == 0:
            sentence = " NO  RECORD  FOUND  WITHIN  THE  DATES."
            my_list.insert(END, sentence)
        lb4 = Label(sub10, text=f"Total Fee Submitted = {fee_amount}", font=('San Fransisco', '12'))
        lb4.place(relx=0.4, rely=0.85)
        my_list.place(relx=0.135, rely=0.18, relwidth=0.714, relheight=0.61)
        scroll_bar.config(command=my_list.yview)
        sub9.withdraw()

    conn = sq.connect('records.db')
    c = conn.cursor()
    global sub9
    sub9 = Toplevel()
    sub9.geometry('900x650+200+20')
    sub9.title('Fee Record')
    frame8 = LabelFrame(sub9, text='Fee Record', font=('San Fransisco', '15'))
    frame8.place(relx=0.1, rely=0.085, relwidth=0.8, relheight=0.85)
    bt1 = Button(sub9, command=back, text='Back', font=('San Fransisco', '10'))
    bt1.place(relx=0.135, rely=0.85, relwidth=0.1)
    bt2 = Button(sub9, command=next, text='Next', font=('San Fransisco', '10'))
    bt2.place(relx=0.765, rely=0.85, relwidth=0.1)
    lb1 = Label(sub9, text='From (Date)-', font=('San Fransisco', '10'))
    lb1.place(relx=0.36, rely=0.35)
    from_var = StringVar()
    from_var.set("dd/mm/yyyy")
    en1 = Entry(sub9, textvariable=from_var, font=('San Fransisco', '10'))
    en1.place(relx=0.47, rely=0.35, relwidth=0.15)
    lb2 = Label(sub9, text="To (Date)-", font=('San Fransisco', '10'))
    lb2.place(relx=0.36, rely=0.42)
    to_var = StringVar()
    to_var.set("dd/mm/yyyy")
    en3 = Entry(sub9, textvariable=to_var, font=('San Fransisco', '10'))
    en3.place(relx=0.47, rely=0.42, relwidth=0.15)
    submitted_by_var = StringVar()
    submitted_by_var.set('All')
    all_submitted = ['Myself', 'All']
    lb3 = Label(sub9, text='Submitted by-', font=('San Fransisco', '10'))
    lb3.place(relx=0.36, rely=0.499)
    drop1 = OptionMenu(sub9, submitted_by_var, *all_submitted)
    drop1.place(relx=0.47, rely=0.49, relwidth=0.15)
    home.withdraw()


######################################################################################################


# ################################---------edit_course---------#######################################

def edit_course():
    def edit_course_window_next():
        def edit_course_window_submit():
            duration = duration_var.get()
            rfee = rfee_var.get()
            ins1 = ins1_var.get()
            ins2 = ins2_var.get()
            ins3 = ins3_var.get()
            ins4 = ins4_var.get()
            ins5 = ins5_var.get()
            ins6 = ins6_var.get()
            ins7 = ins7_var.get()
            ins8 = ins8_var.get()
            ins9 = ins9_var.get()
            ins10 = ins10_var.get()
            ins11 = ins11_var.get()
            ins12 = ins12_var.get()
            ins13 = ins13_var.get()
            ins14 = ins14_var.get()
            ins15 = ins15_var.get()
            ins16 = ins16_var.get()
            ins17 = ins17_var.get()
            ins18 = ins18_var.get()
            if duration == '':
                messagebox.showerror("Error", "Enter duration")
            elif duration == 'mm' or len(duration) < 2 or duration.isdigit() is not True:
                messagebox.showerror("Error", "Invalid duration")
            elif rfee == '':
                messagebox.showerror("Error", "Reg. fee can't be empty")
            elif rfee.isdigit() is not True:
                messagebox.showerror("Error", "Invalid Reg. Fee")
            elif ins1 == '':
                messagebox.showerror("Error", "Installment-1 can't be empty")
            elif ins1.isdigit() is not True:
                messagebox.showerror("Error", "Invalid Installment-1")
            elif ins2 == '':
                messagebox.showerror("Error", "Installment-2 can't be empty")
            elif ins2.isdigit() is not True:
                messagebox.showerror("Error", "Invalid Installment-2")
            elif ins3 == '':
                messagebox.showerror("Error", "Installment-3 can't be empty")
            elif ins3.isdigit() is not True:
                messagebox.showerror("Error", "Invalid Installment-3")
            elif ins4 == '':
                messagebox.showerror("Error", "Installment-4 can't be empty")
            elif ins4.isdigit() is not True:
                messagebox.showerror("Error", "Invalid Installment-4")
            elif ins5 == '':
                messagebox.showerror("Error", "Installment-5 can't be empty")
            elif ins5.isdigit() is not True:
                messagebox.showerror("Error", "Invalid Installment-5")
            elif ins6 == '':
                messagebox.showerror("Error", "Installment-6 can't be empty")
            elif ins6.isdigit() is not True:
                messagebox.showerror("Error", "Invalid Installment-6")
            elif ins7 == '':
                messagebox.showerror("Error", "Installment-7 can't be empty")
            elif ins7.isdigit() is not True:
                messagebox.showerror("Error", "Invalid Installment-7")
            elif ins8 == '':
                messagebox.showerror("Error", "Installment-8 can't be empty")
            elif ins8.isdigit() is not True:
                messagebox.showerror("Error", "Invalid Installment-8")
            elif ins9 == '':
                messagebox.showerror("Error", "Installment-9 can't be empty")
            elif ins9.isdigit() is not True:
                messagebox.showerror("Error", "Invalid Installment-9")
            elif ins10 == '':
                messagebox.showerror("Error", "Installment-10 can't be empty")
            elif ins10.isdigit() is not True:
                messagebox.showerror("Error", "Invalid Installment-10")
            elif ins11.isdigit() is not True:
                messagebox.showerror("Error", "Installment-11 can't be empty")
            elif ins11 == '':
                messagebox.showerror("Error", "Enter Installment-11")
            elif ins12 == '':
                messagebox.showerror("Error", "Installment-12 can't be empty")
            elif ins12.isdigit() is not True:
                messagebox.showerror("Error", "Invalid Installment-12")
            elif ins13 == '':
                messagebox.showerror("Error", "Installment-13 can't be empty")
            elif ins13.isdigit() is not True:
                messagebox.showerror("Error", "Invalid Installment-13")
            elif ins14 == '':
                messagebox.showerror("Error", "Installment-14 can't be empty")
            elif ins14.isdigit() is not True:
                messagebox.showerror("Error", "Invalid Installment-14")
            elif ins15 == '':
                messagebox.showerror("Error", "Installment-15 can't be empty")
            elif ins15.isdigit() is not True:
                messagebox.showerror("Error", "Invalid Installment-15")
            elif ins16 == '':
                messagebox.showerror("Error", "Installment-16 can't be empty")
            elif ins16.isdigit() is not True:
                messagebox.showerror("Error", "Invalid Installment-16")
            elif ins17 == '':
                messagebox.showerror("Error", "Installment-17 can't be empty")
            elif ins17.isdigit() is not True:
                messagebox.showerror("Error", "Invalid Installment-17")
            elif ins18 == '':
                messagebox.showerror("Error", "Installment-18 can't be empty")
            elif ins18.isdigit() is not True:
                messagebox.showerror("Error", "Invalid Installment-18")
            else:
                ans = messagebox.askquestion("Are u sure", "Do You Want To Submit?")
                if ans == "yes":
                    command2 = "UPDATE FEE_STRUCTURE10 SET DURATION=?,REG00=?,INS01=?,INS02=?,INS03=?,INS04=?,INS05=?" \
                               ",INS06=?,INS07=?,INS08=?,INS09=?,INS010=?,INS011=?,INS012=?,INS013=?,INS014=?" \
                               ",INS015=?,INS016=?,INS017=?,INS018=? WHERE COURSE_NAME=?"
                    data_tuple2 = (duration, rfee, ins1, ins2, ins3, ins4, ins5, ins6, ins7, ins8, ins9,
                                   ins10, ins11, ins12, ins13, ins14, ins15, ins16, ins17, ins18, course)
                    c.execute(command2, data_tuple2)
                    conn.commit()
                    c.close()
                    conn.close()
                    edit_course_window.destroy()
                    more_window.deiconify()
                    messagebox.showinfo("Success", "Course edited successfully.")

        course = courses_var.get()
        if course == 'Select course-':
            messagebox.showerror("Error", "Select Course")
        else:
            command = "SELECT * FROM FEE_STRUCTURE10 WHERE COURSE_NAME=?"
            data_tuple = course,
            c.execute(command, data_tuple)
            record = c.fetchall()[0]
            fee_details = []
            for det in record:
                fee_details.append(det)
            lb2 = Label(edit_course_window, text="Duration-", font=('San Fransisco', 10))
            lb2.place(relx=0.35, rely=0.25)
            duration_var = StringVar()
            duration_var.set(fee_details[1][0:2])
            en2 = Entry(edit_course_window, textvariable=duration_var, font=('San Fransisco', '10'))
            en2.place(relx=0.46, rely=0.25, relwidth=0.18)
            lb3 = Label(edit_course_window, text="Reg. Fee-", font=('San Fransisco', 10))
            lb3.place(relx=0.35, rely=0.3)
            rfee_var = StringVar()
            rfee_var.set(fee_details[2])
            en3 = Entry(edit_course_window, textvariable=rfee_var, font=('San Fransisco', '10'))
            en3.place(relx=0.46, rely=0.3, relwidth=0.09)
            lb4 = Label(edit_course_window, text="Installment 1-", font=('San Fransisco', '10'))
            lb4.place(relx=0.135, rely=0.45)
            ins1_var = StringVar()
            ins1_var.set(fee_details[3])
            en4 = Entry(edit_course_window, textvariable=ins1_var, font=('San Fransisco', '10'))
            en4.place(relx=0.24, rely=0.45, relwidth=0.09)
            lb5 = Label(edit_course_window, text="Installment 2-", font=('San Fransisco', '10'))
            lb5.place(relx=0.135, rely=0.5)
            ins2_var = StringVar()
            ins2_var.set(fee_details[4])
            en5 = Entry(edit_course_window, textvariable=ins2_var, font=('San Fransisco', '10'))
            en5.place(relx=0.24, rely=0.5, relwidth=0.09)
            lb6 = Label(edit_course_window, text="Installment 3-", font=('San Fransisco', '10'))
            lb6.place(relx=0.135, rely=0.55)
            ins3_var = StringVar()
            ins3_var.set(fee_details[5])
            en6 = Entry(edit_course_window, textvariable=ins3_var, font=('San Fransisco', '10'))
            en6.place(relx=0.24, rely=0.55, relwidth=0.09)
            lb7 = Label(edit_course_window, text="Installment 4-", font=('San Fransisco', '10'))
            lb7.place(relx=0.135, rely=0.6)
            ins4_var = StringVar()
            ins4_var.set(fee_details[6])
            en7 = Entry(edit_course_window, textvariable=ins4_var, font=('San Fransisco', '10'))
            en7.place(relx=0.24, rely=0.6, relwidth=0.09)
            lb8 = Label(edit_course_window, text="Installment 5-", font=('San Fransisco', '10'))
            lb8.place(relx=0.135, rely=0.65)
            ins5_var = StringVar()
            ins5_var.set(fee_details[7])
            en8 = Entry(edit_course_window, textvariable=ins5_var, font=('San Fransisco', '10'))
            en8.place(relx=0.24, rely=0.65, relwidth=0.09)
            lb8i = Label(edit_course_window, text="Installment 6-", font=('San Fransisco', '10'))
            lb8i.place(relx=0.135, rely=0.7)
            ins6_var = StringVar()
            ins6_var.set(fee_details[8])
            en8i = Entry(edit_course_window, textvariable=ins6_var, font=('San Fransisco', '10'))
            en8i.place(relx=0.24, rely=0.7, relwidth=0.09)
            lb9 = Label(edit_course_window, text="Installment 7-", font=('San Fransisco', '10'))
            lb9.place(relx=0.39, rely=0.45)
            ins7_var = StringVar()
            ins7_var.set(fee_details[9])
            en9 = Entry(edit_course_window, textvariable=ins7_var, font=('San Fransisco', '10'))
            en9.place(relx=0.5, rely=0.45, relwidth=0.09)
            lb10 = Label(edit_course_window, text="Installment 8-", font=('San Fransisco', '10'))
            lb10.place(relx=0.39, rely=0.5)
            ins8_var = StringVar()
            ins8_var.set(fee_details[10])
            en10 = Entry(edit_course_window, textvariable=ins8_var, font=('San Fransisco', '10'))
            en10.place(relx=0.5, rely=0.5, relwidth=0.09)
            lb11 = Label(edit_course_window, text="Installment 9-", font=('San Fransisco', '10'))
            lb11.place(relx=0.39, rely=0.55)
            ins9_var = StringVar()
            ins9_var.set(fee_details[11])
            en11 = Entry(edit_course_window, textvariable=ins9_var, font=('San Fransisco', '10'))
            en11.place(relx=0.5, rely=0.55, relwidth=0.09)
            lb12 = Label(edit_course_window, text="Installment 10-", font=('San Fransisco', '10'))
            lb12.place(relx=0.39, rely=0.6)
            ins10_var = StringVar()
            ins10_var.set(fee_details[12])
            en12 = Entry(edit_course_window, textvariable=ins10_var, font=('San Fransisco', '10'))
            en12.place(relx=0.5, rely=0.6, relwidth=0.09)
            lb13 = Label(edit_course_window, text="Installment 11-", font=('San Fransisco', '10'))
            lb13.place(relx=0.39, rely=0.65)
            ins11_var = StringVar()
            ins11_var.set(fee_details[13])
            en13 = Entry(edit_course_window, textvariable=ins11_var, font=('San Fransisco', '10'))
            en13.place(relx=0.5, rely=0.65, relwidth=0.09)
            lb14 = Label(edit_course_window, text="Installment 12-", font=('San Fransisco', '10'))
            lb14.place(relx=0.39, rely=0.7)
            ins12_var = StringVar()
            ins12_var.set(fee_details[14])
            en14 = Entry(edit_course_window, textvariable=ins12_var, font=('San Fransisco', '10'))
            en14.place(relx=0.5, rely=0.7, relwidth=0.09)
            lb15 = Label(edit_course_window, text="Installment 13-", font=('San Fransisco', '10'))
            lb15.place(relx=0.655, rely=0.45)
            ins13_var = StringVar()
            ins13_var.set(fee_details[15])
            en15 = Entry(edit_course_window, textvariable=ins13_var, font=('San Fransisco', '10'))
            en15.place(relx=0.765, rely=0.45, relwidth=0.09)
            lb16 = Label(edit_course_window, text="Installment 14-", font=('San Fransisco', '10'))
            lb16.place(relx=0.655, rely=0.5)
            ins14_var = StringVar()
            ins14_var.set(fee_details[16])
            en16 = Entry(edit_course_window, textvariable=ins14_var, font=('San Fransisco', '10'))
            en16.place(relx=0.765, rely=0.5, relwidth=0.09)
            lb17 = Label(edit_course_window, text="Installment 15-", font=('San Fransisco', '10'))
            lb17.place(relx=0.655, rely=0.55)
            ins15_var = StringVar()
            ins15_var.set(fee_details[17])
            en17 = Entry(edit_course_window, textvariable=ins15_var, font=('San Fransisco', '10'))
            en17.place(relx=0.765, rely=0.55, relwidth=0.09)
            lb18 = Label(edit_course_window, text="Installment 16-", font=('San Fransisco', '10'))
            lb18.place(relx=0.655, rely=0.6)
            ins16_var = StringVar()
            ins16_var.set(fee_details[18])
            en18 = Entry(edit_course_window, textvariable=ins16_var, font=('San Fransisco', '10'))
            en18.place(relx=0.765, rely=0.6, relwidth=0.09)
            lb19 = Label(edit_course_window, text="Installment 17-", font=('San Fransisco', '10'))
            lb19.place(relx=0.655, rely=0.65)
            ins17_var = StringVar()
            ins17_var.set(fee_details[19])
            en19 = Entry(edit_course_window, textvariable=ins17_var, font=('San Fransisco', '10'))
            en19.place(relx=0.765, rely=0.65, relwidth=0.09)
            lb20 = Label(edit_course_window, text="Installment 18-", font=('San Fransisco', '10'))
            lb20.place(relx=0.655, rely=0.7)
            ins18_var = StringVar()
            ins18_var.set(fee_details[20])
            en20 = Entry(edit_course_window, textvariable=ins18_var, font=('San Fransisco', '10'))
            en20.place(relx=0.765, rely=0.7, relwidth=0.09)
            bt3 = Button(edit_course_window, text='Submit', command=edit_course_window_submit,
                         font=('San Fransisco', '10'), fg="BLUE")
            bt3.place(relx=0.765, rely=0.85, relwidth=0.1)

    def edit_course_window_back():
        c.close()
        conn.close()
        more_window.deiconify()
        edit_course_window.destroy()

    global edit_course_window
    conn = sq.connect('records.db')
    c = conn.cursor()
    edit_course_window = Toplevel()
    edit_course_window.geometry('900x650+200+20')
    edit_course_window.title('Edit Course')
    edit_course_frame = LabelFrame(edit_course_window, text="edit course", font=('San Fransisco', '15'))
    edit_course_frame.place(relx=0.1, rely=0.085, relwidth=0.8, relheight=0.85)
    lb1 = Label(edit_course_window, text='Course -', font=('San Fransisco', 10))
    lb1.place(relx=0.35, rely=0.2)
    c.execute("SELECT COURSE_NAME FROM FEE_STRUCTURE10;")
    all_courses = []
    r = c.fetchall()
    for i in r:
        all_courses.append(i[0])
    courses_var = StringVar()
    courses_var.set('Select course-')
    drop1 = OptionMenu(edit_course_window, courses_var, *all_courses)
    drop1.place(relx=0.46, rely=0.20, relwidth=0.18)
    bt1 = Button(edit_course_window, text='Next', command=edit_course_window_next, font=('San Fransisco', '10'))
    bt1.place(relx=0.7, rely=0.2, relwidth=0.1)
    bt2 = Button(edit_course_window, text='Back', command=edit_course_window_back, font=('San Fransisco', '10'))
    bt2.place(relx=0.135, rely=0.85, relwidth=0.1)
    more_window.withdraw()


######################################################################################################


# ################################---------new_course---------#########################################

def new_course(admin='none'):
    def new_course_window_logout():
        c.close()
        conn.close()
        new_course_window.destroy()
        login_window()

    def new_course_window_back():
        c.close()
        conn.close()
        more_window.deiconify()
        new_course_window.destroy()

    def new_course_window_submit():
        course_name = course_name_var.get()
        duration = duration_var.get()
        rfee = rfee_var.get()
        ins1 = ins1_var.get()
        ins2 = ins2_var.get()
        ins3 = ins3_var.get()
        ins4 = ins4_var.get()
        ins5 = ins5_var.get()
        ins6 = ins6_var.get()
        ins7 = ins7_var.get()
        ins8 = ins8_var.get()
        ins9 = ins9_var.get()
        ins10 = ins10_var.get()
        ins11 = ins11_var.get()
        ins12 = ins12_var.get()
        ins13 = ins13_var.get()
        ins14 = ins14_var.get()
        ins15 = ins15_var.get()
        ins16 = ins16_var.get()
        ins17 = ins17_var.get()
        ins18 = ins18_var.get()
        if course_name == '':
            messagebox.showerror("Error", "Enter course name")
        elif duration == '':
            messagebox.showerror("Error", "Enter duration")
        elif duration == 'mm' or len(duration) < 2 or duration.isdigit() is not True:
            messagebox.showerror("Error", "Invalid duration")
        elif rfee == '':
            messagebox.showerror("Error", "Enter Reg. fee")
        elif rfee.isdigit() is not True:
            messagebox.showerror("Error", "Invalid Reg. Fee")
        elif ins1 == '':
            messagebox.showerror("Error", "Enter Installment-1")
        elif ins1.isdigit() is not True:
            messagebox.showerror("Error", "Invalid Installment-1")
        elif ins2 == '':
            messagebox.showerror("Error", "Enter Installment-2")
        elif ins2.isdigit() is not True:
            messagebox.showerror("Error", "Invalid Installment-2")
        elif ins3 == '':
            messagebox.showerror("Error", "Enter Installment-3")
        elif ins3.isdigit() is not True:
            messagebox.showerror("Error", "Invalid Installment-3")
        elif ins4 == '':
            messagebox.showerror("Error", "Enter Installment-4")
        elif ins4.isdigit() is not True:
            messagebox.showerror("Error", "Invalid Installment-4")
        elif ins5 == '':
            messagebox.showerror("Error", "Enter Installment-5")
        elif ins5.isdigit() is not True:
            messagebox.showerror("Error", "Invalid Installment-5")
        elif ins6 == '':
            messagebox.showerror("Error", "Enter Installment-6")
        elif ins6.isdigit() is not True:
            messagebox.showerror("Error", "Invalid Installment-6")
        elif ins7 == '':
            messagebox.showerror("Error", "Enter Installment-7")
        elif ins7.isdigit() is not True:
            messagebox.showerror("Error", "Invalid Installment-7")
        elif ins8 == '':
            messagebox.showerror("Error", "Enter Installment-8")
        elif ins8.isdigit() is not True:
            messagebox.showerror("Error", "Invalid Installment-8")
        elif ins9 == '':
            messagebox.showerror("Error", "Enter Installment-9")
        elif ins9.isdigit() is not True:
            messagebox.showerror("Error", "Invalid Installment-9")
        elif ins10 == '':
            messagebox.showerror("Error", "Enter Installment-10")
        elif ins10.isdigit() is not True:
            messagebox.showerror("Error", "Invalid Installment-10")
        elif ins11.isdigit() is not True:
            messagebox.showerror("Error", "Invalid Installment-11")
        elif ins11 == '':
            messagebox.showerror("Error", "Enter Installment-11")
        elif ins12 == '':
            messagebox.showerror("Error", "Enter Installment-12")
        elif ins12.isdigit() is not True:
            messagebox.showerror("Error", "Invalid Installment-12")
        elif ins13 == '':
            messagebox.showerror("Error", "Enter Installment-13")
        elif ins13.isdigit() is not True:
            messagebox.showerror("Error", "Invalid Installment-13")
        elif ins14 == '':
            messagebox.showerror("Error", "Enter Installment-14")
        elif ins14.isdigit() is not True:
            messagebox.showerror("Error", "Invalid Installment-14")
        elif ins15 == '':
            messagebox.showerror("Error", "Enter Installment-15")
        elif ins15.isdigit() is not True:
            messagebox.showerror("Error", "Invalid Installment-15")
        elif ins16 == '':
            messagebox.showerror("Error", "Enter Installment-16")
        elif ins16.isdigit() is not True:
            messagebox.showerror("Error", "Invalid Installment-16")
        elif ins17 == '':
            messagebox.showerror("Error", "Enter Installment-17")
        elif ins17.isdigit() is not True:
            messagebox.showerror("Error", "Invalid Installment-17")
        elif ins18 == '':
            messagebox.showerror("Error", "Enter Installment-18")
        elif ins18.isdigit() is not True:
            messagebox.showerror("Error", "Invalid Installment-18")
        else:
            ans = messagebox.askquestion("Are u sure", "Do You Want To Submit?")
            if ans == "yes":
                command = "INSERT INTO FEE_STRUCTURE10  \
                          VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
                data_tuple = (course_name, duration, rfee, ins1, ins2, ins3, ins4, ins5, ins6, ins7, ins8, ins9,
                              ins10, ins11, ins12, ins13, ins14, ins15, ins16, ins17, ins18)
                c.execute(command, data_tuple)
                conn.commit()
                c.close()
                conn.close()
                new_course_window.destroy()
                if okay == 1:
                    home_window(admin)
                else:
                    more_window.deiconify()
                messagebox.showinfo("Success", "New Course Added Successfully to System")

    global new_course_window
    conn = sq.connect('records.db')
    c = conn.cursor()
    new_course_window = Toplevel()
    new_course_window.geometry('900x650+200+20')
    new_course_window.title('New Course')
    new_course_frame = LabelFrame(new_course_window, text="new course", font=('San Fransisco', '15'))
    new_course_frame.place(relx=0.1, rely=0.085, relwidth=0.8, relheight=0.85)
    lb1 = Label(new_course_window, text='Course Name-', font=('San Fransisco', 10))
    lb1.place(relx=0.35, rely=0.2)
    course_name_var = StringVar()
    en1 = Entry(new_course_window, textvariable=course_name_var, font=('San Fransisco', '10'))
    en1.place(relx=0.46, rely=0.2, relwidth=0.18)
    lb2 = Label(new_course_window, text="Duration-", font=('San Fransisco', 10))
    lb2.place(relx=0.35, rely=0.25)
    duration_var = StringVar()
    duration_var.set('mm')
    en2 = Entry(new_course_window, textvariable=duration_var, font=('San Fransisco', '10'))
    en2.place(relx=0.46, rely=0.25, relwidth=0.18)
    lb3 = Label(new_course_window, text="Reg. Fee-", font=('San Fransisco', 10))
    lb3.place(relx=0.35, rely=0.3)
    rfee_var = StringVar()
    rfee_var.set('0')
    en3 = Entry(new_course_window, textvariable=rfee_var, font=('San Fransisco', '10'))
    en3.place(relx=0.46, rely=0.3, relwidth=0.09)
    lb4 = Label(new_course_window, text="Installment 1-", font=('San Fransisco', '10'))
    lb4.place(relx=0.135, rely=0.45)
    ins1_var = StringVar()
    ins1_var.set('0')
    en4 = Entry(new_course_window, textvariable=ins1_var, font=('San Fransisco', '10'))
    en4.place(relx=0.24, rely=0.45, relwidth=0.09)
    lb5 = Label(new_course_window, text="Installment 2-", font=('San Fransisco', '10'))
    lb5.place(relx=0.135, rely=0.5)
    ins2_var = StringVar()
    ins2_var.set('0')
    en5 = Entry(new_course_window, textvariable=ins2_var, font=('San Fransisco', '10'))
    en5.place(relx=0.24, rely=0.5, relwidth=0.09)
    lb6 = Label(new_course_window, text="Installment 3-", font=('San Fransisco', '10'))
    lb6.place(relx=0.135, rely=0.55)
    ins3_var = StringVar()
    ins3_var.set('0')
    en6 = Entry(new_course_window, textvariable=ins3_var, font=('San Fransisco', '10'))
    en6.place(relx=0.24, rely=0.55, relwidth=0.09)
    lb7 = Label(new_course_window, text="Installment 4-", font=('San Fransisco', '10'))
    lb7.place(relx=0.135, rely=0.6)
    ins4_var = StringVar()
    ins4_var.set('0')
    en7 = Entry(new_course_window, textvariable=ins4_var, font=('San Fransisco', '10'))
    en7.place(relx=0.24, rely=0.6, relwidth=0.09)
    lb8 = Label(new_course_window, text="Installment 5-", font=('San Fransisco', '10'))
    lb8.place(relx=0.135, rely=0.65)
    ins5_var = StringVar()
    ins5_var.set('0')
    en8 = Entry(new_course_window, textvariable=ins5_var, font=('San Fransisco', '10'))
    en8.place(relx=0.24, rely=0.65, relwidth=0.09)
    lb8i = Label(new_course_window, text="Installment 6-", font=('San Fransisco', '10'))
    lb8i.place(relx=0.135, rely=0.7)
    ins6_var = StringVar()
    ins6_var.set('0')
    en8i = Entry(new_course_window, textvariable=ins6_var, font=('San Fransisco', '10'))
    en8i.place(relx=0.24, rely=0.7, relwidth=0.09)
    lb9 = Label(new_course_window, text="Installment 7-", font=('San Fransisco', '10'))
    lb9.place(relx=0.39, rely=0.45)
    ins7_var = StringVar()
    ins7_var.set('0')
    en9 = Entry(new_course_window, textvariable=ins7_var, font=('San Fransisco', '10'))
    en9.place(relx=0.5, rely=0.45, relwidth=0.09)
    lb10 = Label(new_course_window, text="Installment 8-", font=('San Fransisco', '10'))
    lb10.place(relx=0.39, rely=0.5)
    ins8_var = StringVar()
    ins8_var.set('0')
    en10 = Entry(new_course_window, textvariable=ins8_var, font=('San Fransisco', '10'))
    en10.place(relx=0.5, rely=0.5, relwidth=0.09)
    lb11 = Label(new_course_window, text="Installment 9-", font=('San Fransisco', '10'))
    lb11.place(relx=0.39, rely=0.55)
    ins9_var = StringVar()
    ins9_var.set('0')
    en11 = Entry(new_course_window, textvariable=ins9_var, font=('San Fransisco', '10'))
    en11.place(relx=0.5, rely=0.55, relwidth=0.09)
    lb12 = Label(new_course_window, text="Installment 10-", font=('San Fransisco', '10'))
    lb12.place(relx=0.39, rely=0.6)
    ins10_var = StringVar()
    ins10_var.set('0')
    en12 = Entry(new_course_window, textvariable=ins10_var, font=('San Fransisco', '10'))
    en12.place(relx=0.5, rely=0.6, relwidth=0.09)
    lb13 = Label(new_course_window, text="Installment 11-", font=('San Fransisco', '10'))
    lb13.place(relx=0.39, rely=0.65)
    ins11_var = StringVar()
    ins11_var.set('0')
    en13 = Entry(new_course_window, textvariable=ins11_var, font=('San Fransisco', '10'))
    en13.place(relx=0.5, rely=0.65, relwidth=0.09)
    lb14 = Label(new_course_window, text="Installment 12-", font=('San Fransisco', '10'))
    lb14.place(relx=0.39, rely=0.7)
    ins12_var = StringVar()
    ins12_var.set('0')
    en14 = Entry(new_course_window, textvariable=ins12_var, font=('San Fransisco', '10'))
    en14.place(relx=0.5, rely=0.7, relwidth=0.09)
    lb15 = Label(new_course_window, text="Installment 13-", font=('San Fransisco', '10'))
    lb15.place(relx=0.655, rely=0.45)
    ins13_var = StringVar()
    ins13_var.set('0')
    en15 = Entry(new_course_window, textvariable=ins13_var, font=('San Fransisco', '10'))
    en15.place(relx=0.765, rely=0.45, relwidth=0.09)
    lb16 = Label(new_course_window, text="Installment 14-", font=('San Fransisco', '10'))
    lb16.place(relx=0.655, rely=0.5)
    ins14_var = StringVar()
    ins14_var.set('0')
    en16 = Entry(new_course_window, textvariable=ins14_var, font=('San Fransisco', '10'))
    en16.place(relx=0.765, rely=0.5, relwidth=0.09)
    lb17 = Label(new_course_window, text="Installment 15-", font=('San Fransisco', '10'))
    lb17.place(relx=0.655, rely=0.55)
    ins15_var = StringVar()
    ins15_var.set('0')
    en17 = Entry(new_course_window, textvariable=ins15_var, font=('San Fransisco', '10'))
    en17.place(relx=0.765, rely=0.55, relwidth=0.09)
    lb18 = Label(new_course_window, text="Installment 16-", font=('San Fransisco', '10'))
    lb18.place(relx=0.655, rely=0.6)
    ins16_var = StringVar()
    ins16_var.set('0')
    en18 = Entry(new_course_window, textvariable=ins16_var, font=('San Fransisco', '10'))
    en18.place(relx=0.765, rely=0.6, relwidth=0.09)
    lb19 = Label(new_course_window, text="Installment 17-", font=('San Fransisco', '10'))
    lb19.place(relx=0.655, rely=0.65)
    ins17_var = StringVar()
    ins17_var.set('0')
    en19 = Entry(new_course_window, textvariable=ins17_var, font=('San Fransisco', '10'))
    en19.place(relx=0.765, rely=0.65, relwidth=0.09)
    lb20 = Label(new_course_window, text="Installment 18-", font=('San Fransisco', '10'))
    lb20.place(relx=0.655, rely=0.7)
    ins18_var = StringVar()
    ins18_var.set('0')
    en20 = Entry(new_course_window, textvariable=ins18_var, font=('San Fransisco', '10'))
    en20.place(relx=0.765, rely=0.7, relwidth=0.09)
    c.execute("SELECT COUNT(*) FROM FEE_STRUCTURE10;")
    fee_check = c.fetchall()[0][0]
    if fee_check == 0:
        bt1 = Button(new_course_window, text='Logout', command=new_course_window_logout,
                     font=('San Fransisco', '10'), fg="RED")
        okay = 1
    else:
        bt1 = Button(new_course_window, text='Back', command=new_course_window_back, font=('San Fransisco', '10'))
        more_window.withdraw()
    bt1.place(relx=0.135, rely=0.85, relwidth=0.1)
    bt2 = Button(new_course_window, text='Submit', command=new_course_window_submit, font=('San Fransisco', '10')
                 , fg="BLUE")
    bt2.place(relx=0.765, rely=0.85, relwidth=0.1)


######################################################################################################


# ####################################---------add_user---------#######################################
def add_user():
    def add_user_window_back():
        c.close()
        conn.close()
        more_window.deiconify()
        add_user_window.destroy()

    def add_user_window_submit():
        new_username = new_username_var.get()
        new_password = new_password_var.get()
        confirm_password = confirm_password_var.get()
        c.execute("SELECT LOGIN_ID FROM LOGIN_CRED;")
        records = c.fetchall()
        ids = []
        for i in records:
            ids.append(i[0])
        if new_username == '':
            messagebox.showerror("Error", "Enter username")
        elif new_username in ids:
            messagebox.showerror("Error", "Username already exists")
        elif new_password == '':
            messagebox.showerror("Error", "Enter password")
        elif confirm_password == '':
            messagebox.showerror("Error", "Enter confirm password")
        elif confirm_password != new_password:
            messagebox.showerror("Error", "Passwords does not match")
        else:
            ans = messagebox.askquestion("Are u sure", "Do You Want To Submit?")
            if ans == "yes":
                command = "INSERT INTO LOGIN_CRED " \
                          "VALUES(?,?);"
                data_tuple = (new_username, new_password)
                c.execute(command, data_tuple)
                conn.commit()
                c.close()
                conn.close()
                add_user_window.destroy()
                more_window.deiconify()
                messagebox.showinfo("Success", "New User Added Successfully to System")

    global add_user_window
    conn = sq.connect('records.db')
    c = conn.cursor()
    add_user_window = Toplevel()
    add_user_window.geometry('900x650+200+20')
    add_user_window.title('Add User')
    add_user_window_frame = LabelFrame(add_user_window, text="add user", font=('San Fransisco', '15'))
    add_user_window_frame.place(relx=0.1, rely=0.085, relwidth=0.8, relheight=0.85)
    bt1 = Button(add_user_window, text='Back', command=add_user_window_back, font=('San Fransisco', '10'))
    bt1.place(relx=0.135, rely=0.85, relwidth=0.1)
    bt2 = Button(add_user_window, text='Submit', command=add_user_window_submit, font=('San Fransisco', '10')
                 , fg="BLUE")
    bt2.place(relx=0.765, rely=0.85, relwidth=0.1)
    lb1 = Label(add_user_window, text='New username-', font=('San Fransisco', '10'))
    lb1.place(relx=0.36, rely=0.34)
    new_username_var = StringVar()
    en1 = Entry(add_user_window, textvariable=new_username_var, font=('San Fransisco', '10'))
    en1.place(relx=0.47, rely=0.339, relwidth=0.15)
    lb2 = Label(add_user_window, text='New password-', font=('San Fransisco', '10'))
    lb2.place(relx=0.36, rely=0.41)
    new_password_var = StringVar()
    en2 = Entry(add_user_window, textvariable=new_password_var, show="•")
    en2.place(relx=0.47, rely=0.405, relwidth=0.15)
    lb3 = Label(add_user_window, text='Confirm password-', font=('San Fransisco', '10'))
    lb3.place(relx=0.36, rely=0.48)
    confirm_password_var = StringVar()
    en3 = Entry(add_user_window, textvariable=confirm_password_var, show="•")
    en3.place(relx=0.47, rely=0.475, relwidth=0.15)
    more_window.withdraw()


#####################################################################################################


# ##################################--------change_password---------#################################
def change_password(user):
    def change_pass_window_back():
        c.close()
        conn.close()
        more_window.deiconify()
        change_pass_window.destroy()

    def change_pass_window_submit():
        old_pass = old_pass_var.get()
        new_password = new_password_var.get()
        confirm_password = confirm_password_var.get()
        command = "SELECT PASSWORD FROM LOGIN_CRED WHERE LOGIN_ID=?;"
        data_tuple = (user,)
        c.execute(command, data_tuple)
        existing_pass = c.fetchall()[0][0]
        if old_pass == '':
            messagebox.showerror("Error", "Enter old password")
        elif old_pass != existing_pass:
            messagebox.showerror("Error", "Old password is incorrect")
        elif new_password == '':
            messagebox.showerror("Error", "Enter new password")
        elif confirm_password == '':
            messagebox.showerror("Error", "Enter confirm password")
        elif confirm_password != new_password:
            messagebox.showerror("Error", "Passwords does not match")
        else:
            ans = messagebox.askquestion("Are u sure", "Do You Want To Submit?")
            if ans == "yes":
                command = "UPDATE LOGIN_CRED SET PASSWORD= ? WHERE LOGIN_ID = ?"
                data_tuple = (new_password, user)
                c.execute(command, data_tuple)
                conn.commit()
                c.close()
                conn.close()
                change_pass_window.destroy()
                more_window.deiconify()
                messagebox.showinfo("Success", "Password changed")

    global change_pass_window
    conn = sq.connect('records.db')
    c = conn.cursor()
    change_pass_window = Toplevel()
    change_pass_window.geometry('900x650+200+20')
    change_pass_window.title('Change Password')
    change_pass_window_frame = LabelFrame(change_pass_window, text="change password", font=('San Fransisco', '15'))
    change_pass_window_frame.place(relx=0.1, rely=0.085, relwidth=0.8, relheight=0.85)
    bt1 = Button(change_pass_window, text='Back', command=change_pass_window_back, font=('San Fransisco', '10'))
    bt1.place(relx=0.135, rely=0.85, relwidth=0.1)
    bt2 = Button(change_pass_window, text='Submit', command=change_pass_window_submit, font=('San Fransisco', '10')
                 , fg="BLUE")
    bt2.place(relx=0.765, rely=0.85, relwidth=0.1)
    lb1 = Label(change_pass_window, text='Old password-', font=('San Fransisco', '10'))
    lb1.place(relx=0.36, rely=0.34)
    old_pass_var = StringVar()
    en1 = Entry(change_pass_window, textvariable=old_pass_var, show="•")
    en1.place(relx=0.47, rely=0.339, relwidth=0.15)
    lb2 = Label(change_pass_window, text='New password-', font=('San Fransisco', '10'))
    lb2.place(relx=0.36, rely=0.41)
    new_password_var = StringVar()
    en2 = Entry(change_pass_window, textvariable=new_password_var, show="•")
    en2.place(relx=0.47, rely=0.405, relwidth=0.15)
    lb3 = Label(change_pass_window, text='Confirm password-', font=('San Fransisco', '10'))
    lb3.place(relx=0.36, rely=0.48)
    confirm_password_var = StringVar()
    en3 = Entry(change_pass_window, textvariable=confirm_password_var, show="•")
    en3.place(relx=0.47, rely=0.475, relwidth=0.15)
    more_window.withdraw()
#####################################################################################################


# ####################################---------more---------#########################################
def more(admin):
    def home_bt():
        home.deiconify()
        more_window.destroy()

    def logout():
        ans = messagebox.askquestion("Are u sure?", "Do You Want to Logout?")
        if ans == "yes":
            more_window.destroy()
            main.destroy()
            login_window()

    global more_window
    more_window = Toplevel()
    more_window.geometry('900x650+200+20')
    more_window.title('More')
    moreframe = LabelFrame(more_window, text="More", font=('San Fransisco', '15'))
    moreframe.place(relx=0.1, rely=0.085, relwidth=0.8, relheight=0.85)
    bt1 = Button(more_window, text='Edit Course', command=edit_course, font=('San Fransisco', 10))
    bt1.place(relx=0.3125, rely=0.3, width=120, height=40)
    bt2 = Button(more_window, text='Add New Course', command=new_course, font=('San Fransisco', 10))
    bt2.place(relx=0.5625, rely=0.3, width=120, height=40)
    bt3 = Button(more_window, text='Add User', command=add_user, font=('San Fransisco', 10))
    bt3.place(relx=0.3125, rely=0.425, width=120, height=40)
    bt4 = Button(more_window, text='Change Password', command=lambda: change_password(admin), font=('San Fransisco', 10))
    bt4.place(relx=0.5625, rely=0.425, width=120, height=40)
    bt5 = Button(more_window, text='Home', command=home_bt, font=('San Fransisco', 10), fg="BLUE")
    bt5.place(relx=0.765, rely=0.85, relwidth=0.1)
    bt6 = Button(more_window, command=logout, text='Logout', font=('San Fransisco', '10'), fg="RED")
    bt6.place(relx=0.135, rely=0.85, relwidth=0.1)
    home.withdraw()


######################################################################################################


# ####################################---------home---------###########################################


def home_window(admin):
    def logout():
        ans = messagebox.askquestion("Are u sure?", "Do You Want to Logout?")
        if ans == "yes":
            home.destroy()
            login_window()

    global home
    home = Toplevel()
    home.geometry('900x650+200+20')
    home.title('Home')
    homeframe = LabelFrame(home, text=f"Hello,{admin}", font=('San Fransisco', '15'))
    homeframe.place(relx=0.1, rely=0.085, relwidth=0.8, relheight=0.85)
    bt1 = Button(home, text='New Admission', command=new_adm, font=('San Fransisco', 10))
    bt1.place(relx=0.3125, rely=0.3, width=120, height=40)
    bt2 = Button(home, text='Fee Submission', command=lambda: fee_sub(admin), font=('San Fransisco', 10))
    bt2.place(relx=0.5625, rely=0.3, width=120, height=40)
    bt3 = Button(home, text='Add Course', command=add_course, font=('San Fransisco', 10))
    bt3.place(relx=0.3125, rely=0.55, width=120, height=40)
    bt4 = Button(home, text='Student Record', command=student_rec, font=('San Fransisco', 10))
    bt4.place(relx=0.3125, rely=0.425, width=120, height=40)
    bt5 = Button(home, text='Pending Fee', command=pending_fee, font=('San Fransisco', 10))
    bt5.place(relx=0.5625, rely=0.55, width=120, height=40)
    bt6 = Button(home, text='Fee Record', command=lambda: fee_record(admin), font=('San Fransisco', 10))
    bt6.place(relx=0.5625, rely=0.425, width=120, height=40)
    bt7 = Button(home, command=logout, text='Logout', font=('San Fransisco', '10'), fg="RED")
    bt7.place(relx=0.135, rely=0.85, relwidth=0.1)
    bt8 = Button(home, command=lambda: more(admin), text='More', font=('San Fransisco', '10'), fg="BLUE")
    bt8.place(relx=0.765, rely=0.85, relwidth=0.1)
    main.destroy()


#########################################################################################################


# ####################################---------login---------#############################################
def login_window():
    def exit_soft():
        c.close()
        conn.close()
        main.destroy()
        root.destroy()

    def login():
        login_id = username_var.get()
        password = password_var.get()
        c.execute("SELECT * FROM LOGIN_CRED;")
        records = c.fetchall()
        login_cred = {}
        for i in records:
            login_cred[i[0]] = i[1]
        if login_id == "" and password == "":
            messagebox.showerror("Error", "Enter Login ID and Password")
        elif login_id == "":
            messagebox.showerror("Error", "Enter Login ID")
        elif login_id not in login_cred:
            messagebox.showerror("Error", "Login ID Not Found")
        elif password == "":
            messagebox.showerror("Error", "Enter Password")
        else:
            if password == login_cred[login_id]:
                c.execute("SELECT COUNT(*) FROM FEE_STRUCTURE10;")
                fee_check = c.fetchall()[0][0]
                if fee_check == 0:
                    new_course(login_id)
                    main.withdraw()
                else:
                    c.close()
                    conn.close()
                    home_window(login_id)
            else:
                messagebox.showerror("Error", "Incorrect Password")

    global main
    main = Toplevel()
    main.geometry('900x650+200+20')
    main.title('login')
    tables()
    conn = sq.connect('records.db')
    c = conn.cursor()
    mainframe = LabelFrame(main, text='Login', font=('San Fransisco', '15'))
    mainframe.place(relx=0.1, rely=0.085, relwidth=0.8, relheight=0.85)
    bt1 = Button(main, command=login, text='Login', font=('San Fransisco', '10'), fg="BLUE")
    bt1.place(relx=0.765, rely=0.85, relwidth=0.1)
    bt2 = Button(main, command=exit_soft, text='Exit', font=('San Fransisco', '10'), fg="RED")
    bt2.place(relx=0.135, rely=0.85, relwidth=0.1)
    lb1 = Label(main, text='Login ID-', font=('San Fransisco', '10'))
    lb1.place(relx=0.36, rely=0.38)
    username_var = StringVar()
    en1 = Entry(main, textvariable=username_var, font=('San Fransisco', '10'))
    en1.place(relx=0.47, rely=0.38, relwidth=0.15)
    lb2 = Label(main, text='Password-', font=('San Fransisco', '10'))
    lb2.place(relx=0.36, rely=0.45)
    password_var = StringVar()
    en2 = Entry(main, textvariable=password_var, show="•")
    en2.place(relx=0.47, rely=0.45, relwidth=0.15)
#########################################################################################################


# ####################################---------new_user---------#########################################

def new_window():
    def new_user_window_exit():
        c.close()
        conn.close()
        new_user_window.destroy()
        root.destroy()

    def new_user_window_submit():
        new_username = new_username_var.get()
        new_password = new_password_var.get()
        confirm_password = confirm_password_var.get()
        c.execute("SELECT LOGIN_ID FROM LOGIN_CRED;")
        records = c.fetchall()
        ids = []
        for i in records:
            ids.append(i[0])
        if new_username == '':
            messagebox.showerror("Error", "Enter username")
        elif new_username in ids:
            messagebox.showerror("Error", "Username already exists")
        elif new_password == '':
            messagebox.showerror("Error", "Enter password")
        elif confirm_password == '':
            messagebox.showerror("Error", "Enter confirm password")
        elif confirm_password != new_password:
            messagebox.showerror("Error", "Passwords does not match")
        else:
            ans = messagebox.askquestion("Are u sure", "Do You Want To Submit?")
            if ans == "yes":
                command = "INSERT INTO LOGIN_CRED " \
                          "VALUES(?,?);"
                data_tuple = (new_username, new_password)
                c.execute(command, data_tuple)
                conn.commit()
                c.close()
                conn.close()
                messagebox.showinfo("Success", "New User Added Successfully to System")
                new_user_window.destroy()
                login_window()


    global new_user_window
    conn = sq.connect('records.db')
    c = conn.cursor()
    new_user_window = Toplevel()
    new_user_window.geometry('900x650+200+20')
    new_user_window.title('New User')
    new_user_window_frame = LabelFrame(new_user_window, text="new user", font=('San Fransisco', '15'))
    new_user_window_frame.place(relx=0.1, rely=0.085, relwidth=0.8, relheight=0.85)
    bt1 = Button(new_user_window, text='Exit', command=new_user_window_exit, font=('San Fransisco', '10'), fg="RED")
    bt1.place(relx=0.135, rely=0.85, relwidth=0.1)
    bt2 = Button(new_user_window, text='Submit', command=new_user_window_submit, font=('San Fransisco', '10')
                 , fg="BLUE")
    bt2.place(relx=0.765, rely=0.85, relwidth=0.1)
    lb1 = Label(new_user_window, text='New username-', font=('San Fransisco', '10'))
    lb1.place(relx=0.36, rely=0.34)
    new_username_var = StringVar()
    en1 = Entry(new_user_window, textvariable=new_username_var, font=('San Fransisco', '10'))
    en1.place(relx=0.47, rely=0.339, relwidth=0.15)
    lb2 = Label(new_user_window, text='New password-', font=('San Fransisco', '10'))
    lb2.place(relx=0.36, rely=0.41)
    new_password_var = StringVar()
    en2 = Entry(new_user_window, textvariable=new_password_var, show="•")
    en2.place(relx=0.47, rely=0.405, relwidth=0.15)
    lb3 = Label(new_user_window, text='Confirm password-', font=('San Fransisco', '10'))
    lb3.place(relx=0.36, rely=0.48)
    confirm_password_var = StringVar()
    en3 = Entry(new_user_window, textvariable=confirm_password_var, show="•")
    en3.place(relx=0.47, rely=0.475, relwidth=0.15)
#########################################################################################################


# ####################################---------check_user---------########################################
def check_user():
    tables()
    conn = sq.connect('records.db')
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM LOGIN_CRED;")
    check = c.fetchall()[0][0]
    if check == 0:
        return True
#########################################################################################################


if check_user():
    new_window()
else:
    login_window()

root.mainloop()
