from tkinter import *
import tkinter.messagebox
import random

#function for level1
def start_game():
    top=Toplevel()
    top.title("Level 1")
    top.geometry("800x800")
    l1_head=Label(top,text="Level 1",fg="red",font=("calibri",30,"bold"))
    l1_head.pack()
    #List of questions
    que = ["PDF stands for _____",
           "USB stands for _____",
           "Frist AI Programming language is ____",
           "Who is the developer of C language",
           "Types of machiene learning?",
           "1cm=____m",
           "What is the formula speed ?",
           "Father of Indian Navy____",
           "Corona Virus spread from which country?",
           "Second largest peak in world____"]

    # list of options
    opt = [["Portable Document Form", "Personal Document Form", "Personal Document Format"],
           ["Universal Serial Bus", "Uniform Source Byte", "Universal Serial Byte"],
           ["IPL", "LISP", "C"],
           ["John McCarthy ", "Dennis Ritchie", "Google"],
           ["Supervised learning ", "Unsuperised learning ", "both"],
           ["100", "50", "0.01"],
           ["distance / time", "power * time", "time * distance"],
           ["Shahu Maharaj", "Sambhaji Raje", "Shivaji Maharaj"],
           ["India", "China", "USA"],
           ["k2", "Annapurna", "Nanda Devi"]]
    k=10
    j=10
    # loop to retrieve randomly question from list
    for i in range(0, 5):
        while j <= 650:
             r = random.choice(que)
             index = que.index(r)
             a = opt[index]
             l2 = Label(top, text=r, fg="blue", font=("calibri", 18, "bold"))
             l2.pack()
             l2.place(x=400, y=70 + j)
             j += 130
             r1 = Radiobutton(top, text=a[0], fg="purple", font=("calibri", 15, "bold"), variable=v, value=a[0],command=check)
             r2 = Radiobutton(top, text=a[1], fg="purple", font=("calibri", 15, "bold"), variable=v, value=a[1],command=check)
             r3 = Radiobutton(top, text=a[2], fg="purple", font=("calibri", 15, "bold"), variable=v, value=a[2],command=check)
             r1.pack()
             r2.pack()
             r3.pack()

             r1.place(x=400, y=100 + k)
             r2.place(x=400, y=130 + k)
             r3.place(x=400, y=160 + k)
             k += 130
            
    btn=Button(top,text="Submit",font=("times new roman",15,"bold"),command=level1_cal, width=15)
    btn.pack()
    btn.place(x=680,y=750)
    
#function of level2
def level2():
    top=Toplevel()
    top.title("Level 2")
    top.geometry("800x800")
    l1_head=Label(top,text="Level 2",fg="red",font=("calibri",30,"bold"))
    l1_head.pack()
    #List of questions
    que = ["National ruler development institute is situated at _______",
           "Which is the single integrated circuit",
           "UNIVAC is the example of ",
           "The first movie released in 1982 with terrific computer animation and graphics was ",
           "2, 3, 6, 18, 109, 1944, 209952",
           "Who has been appointed has a chief secretary of Madhya Pradesh",
           "Which State has announced to give Rs 6 Crore to those winning gold medals at Olympics 2020",
           "What is made of water but if you put it into water it will die?",
           "Total number of Blood groups are",
           "The world smallest country is"]

    # list of options
    opt = [["Patna", "Hyderabad", "New Delhi"],
           ["GATE", "Chip", "CPU"],
           ["2nd Generation Computers", "1st Generation Computers", "3rd Generation Computers"],
           ["Star Wars", "Tron", "Dark Star"],
           ["6", "18", "1944"],
           ["M Gopal Reddy", "Ravi Dubey", "Sheela Mahajan"],
           ["Maharashtra", "Harayana", "Kerala"],
           ["Paper", "Leaf", "Ice Cube"],
           ["9", "8", "10"],
           ["Canada", "Vatican City", "Maldives"]]

    level2_ans=["Hyderabad","GATE","1st Generation Computers","Star Wars","1944","M Gopal Reddy","Haryana","Ice Cube","9","Vatican City"]
    k=10
    j=10
    # loop to retrieve randomly question from list
    for i in range(0, 5):
        while j <= 650:
             r = random.choice(que)
             index = que.index(r)
             a = opt[index]
             l2 = Label(top, text=r, fg="blue", font=("times new roman", 18, "bold"))
             l2.pack()
             l2.place(x=300, y=70 + j)
             j += 130
             r1 = Radiobutton(top, text=a[0], fg="purple", font=("times new roman", 15, "bold"), variable=v, value=a[0],command=level2_check)
             r2 = Radiobutton(top, text=a[1], fg="purple", font=("times new roman", 15, "bold"), variable=v, value=a[1],command=level2_check)
             r3 = Radiobutton(top, text=a[2], fg="purple", font=("times new roman", 15, "bold"), variable=v, value=a[2],command=level2_check)
             r1.pack()
             r2.pack()
             r3.pack()

             r1.place(x=300, y=100 + k)
             r2.place(x=300, y=130 + k)
             r3.place(x=300, y=160 + k)
             k += 130
            
    btn=Button(top,text="Submit",font=("times new roman",15,"bold"),command=level2_cal,width=15)
    btn.pack()
    btn.place(x=680,y=700)

#function of level3
def level3():
    top=Toplevel()
    top.title("Level 2")
    top.geometry("800x800")
    l3_head=Label(top,text="Level 3",fg="red",font=("calibri",30,"bold"))
    l3_head.pack()
    #List of questions
    que = ["In which decade with the first transatlantic radio broadcast occur ?",
           ".MOV extension refers usually to what kind of file ?",
           "Which of the following is a non-metal that remains liquid at room temperature ?",
           "Tetraethyl lead is used as ",
           "Who is the first Indian women to win an Asian Games goldin 400m run ?",
           "Who inevnted the Ballpoint Pen ?",
           "Water acquires a taste on account of the _______ dissolved in it",
           "The country which is known as 'The land of Windmills' is ________",
           "The instrument used by sailors when at sea to show direction is called",
           "The first Chinese pilgrim to come to India was "]

    # list of options
    opt = [["1860s", "1900s", "1850s"],
            ["Animation/movie file", "Audion file", "Image file"],
            ["Helium", "Chlorine", "Bromine"],
           ["petrol additive", "pain killer", "fire extinguisher"],
           ["K. Malleshwari", "Kamaljit Sandhu", "P.T.Usha"],
           ["Write Brothers", "Bicc Brothers", "Biro Brothers"],
           ["Sugar", "Salt", "None of the above"],
           ["Netherlands", "Greenland", "Nepal"],
           ["Microscope", "Mariners Compass", "Telescope"],
           ["Hiuen Tsang", "Fahien", "Sun Yat Sing"]]

    k=10
    j=10
    # loop to retrieve randomly question from list
    for i in range(0, 5):
        while j <= 650:
             r = random.choice(que)
             index = que.index(r)
             a = opt[index]
             l3 = Label(top, text=r, fg="blue", font=("times new roman", 18, "bold"))
             l3.pack()
             l3.place(x=300, y=70 + j)
             j += 130
             r1 = Radiobutton(top, text=a[0], fg="purple", font=("times new roman", 15, "bold"), variable=v, value=a[0],command=level3_check)
             r2 = Radiobutton(top, text=a[1], fg="purple", font=("times new roman", 15, "bold"), variable=v, value=a[1],command=level3_check)
             r3 = Radiobutton(top, text=a[2], fg="purple", font=("times new roman", 15, "bold"), variable=v, value=a[2],command=level3_check)
             r1.pack()
             r2.pack()
             r3.pack()

             r1.place(x=300, y=100 + k)
             r2.place(x=300, y=130 + k)
             r3.place(x=300, y=160 + k)
             k += 130
            
    btn=Button(top,text="Submit",font=("times new roman",15,"bold"),command=level3_cal,width=15)
    btn.pack()
    btn.place(x=680,y=700)
  
#function to calculate score for level1
def level1_cal():
    l=str(len(level1_score))
    msg="Congratulations!! You have scored "+l
    tkinter.messagebox.showinfo('Quiz Game',msg)
    if len(level1_score)>3:
        demo=tkinter.messagebox.askquestion('Quiz Game','Do you want to continue with next level')
        if demo=='yes':
            level2()
        else:
            print("You like to quit")

#function to calculate score for level2
def level2_cal():
    l=str(len(level2_score))
    msg="Congratulations!! You have scored "+l
    tkinter.messagebox.showinfo('Quiz Game',msg)
    if len(level2_score)>3:
        demo=tkinter.messagebox.askquestion('Quiz Game','Do you want to continue with next level')
        if demo=='yes':
            level3()
        else:
            print("You like to quit")

#function to calculate score for level3      
def level3_cal():
    l=str(len(level3_score))
    msg="Congratulations!! You have scored "+l
    tkinter.messagebox.showinfo('Quiz Game',msg)
    if len(level3_score)>3:
        demo=tkinter.messagebox.askquestion('Quiz Game','Congratulations!!! You have successfully completed 3 levels\n Do you want view your certificate')
        if demo=='yes':
            certificate()
        
#variable to store scores     
level1_score=[]
level2_score=[]
level3_score=[]

#function to check correct answers for level1 
def check():
    ans=["Portable Document Form",
         "Universal Serial Bus",
         "LISP",
         "Dennis Ritchie",
         "both",
         "0.01",
         "distance / time",
         "Shivaji Maharaj",
         "China",
         "k2"]
    answer=v.get()
    if answer in ans:
        level1_score.append(answer)

#function to check correct answer for level2
def level2_check():
    level2_ans=["Hyderabad",
                "GATE",
                "1st Generation Computers",
                "Star Wars",
                "1944",
                "M Gopal Reddy",
                "Haryana",
                "Ice Cube",
                "9",
                "Vatican City"]
    level2_answer=v.get()
    if level2_answer in level2_ans:
        level2_score.append(level2_answer)

#function to calculate score for level3
def level3_check():
    level3_ans=["1900s","Animation/movie file","Bromine","petrol additive","Kamaljit Sandhu","Biro Brothers","Salt","Netherlands","Mariners Compass","Fahein"]
    level3_answer=v.get()
    if level3_answer in level3_ans:
        level3_score.append(level3_answer)

#Function to display certificate
def certificate():
    canvas=Canvas(width=300,height=300, bg='white')
    canvas.pack(expand=YES,fill=BOTH)
    canvas.create_rectangle(150,80,1400,700,width=3, fill='white')
    
    title=Label(canvas,text="Certificate of Achievement",fg="blue",font=("Edwardian Script ITC",55), bg='white')
    title.pack()
    title.place(x=500,y=120)
    
    l4=Label(canvas,text="Is hereby granted to",fg="red",font=("calibri",30), bg='white')
    l4.pack()
    l4.place(x=600,y=240)

    nm=txt_name.get()
    label_name=Label(canvas,text=nm,fg="blue",font=("calibri",35,"underline"), bg='white')
    label_name.pack()
    label_name.place(x=720,y=330)
    
    des1=Label(canvas,text="For Outstanding performance in",fg="red",font=("calibri",30), bg='white')
    des1.pack()
    des1.place(x=520,y=420)
    
    des2=Label(canvas,text="Quiz Game",fg="red",font=("calibri",30), bg='white')
    des2.pack()
    des2.place(x=680,y=520)
    
#creates a frame to place controls   
root=Tk()
root.title("Quiz Game")
root.resizable(width=TRUE,height=TRUE)
root.geometry("800x800")
head=Label(root,text="Welcome to Quiz Game",fg="blue",font=("calibri",30,"bold"))
head.pack()
name=Label(root,text="Enter Name : ",fg="red",font=("calibri",19,"bold"))
name.pack()
name.place(x=600,y=200)
txt_name=Entry(root,width=30)
txt_name.pack()
txt_name.place(x=760,y=210)
v = StringVar()
v.set(3)

# button to start the game
btn_start=Button(root,text="Start",font=("times new roman",20,"bold"),width=10,command=start_game)
btn_start.pack()
btn_start.place(x=700,y=400)
root.mainloop()


