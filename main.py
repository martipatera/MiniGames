import tkinter as tk #importuje knihovnu na okno
import random
from PIL import Image, ImageTk

score = None       
variant_text = None
pcwins = 0
userwins = 0   
new_size = (125, 125)

                 
window = tk.Tk() #vytvori zakladni okno        
window.title("GAMES") #tsitle
window.configure(background="#77E4C8")
window.geometry("1200x900")

rock = Image.open("/Users/martinpatera/Projects/MiniGames/rock1Transparent.png")
rock_resized = rock.resize(new_size, Image.LANCZOS)
rockimage = ImageTk.PhotoImage(rock_resized)

paper = Image.open("/Users/martinpatera/Projects/MiniGames/paperTransparent.jpg")
paper_resized = paper.resize(new_size, Image.LANCZOS)
paperimage = ImageTk.PhotoImage(paper_resized)

scissors = Image.open("/Users/martinpatera/Projects/MiniGames/scissorsTransparent.jpeg")
scissors_resized = scissors.resize(new_size, Image.LANCZOS)
scissorsimage = ImageTk.PhotoImage(scissors_resized)



def RockPaperScissorsGame():
    
     
    for buttons in window.winfo_children():
            buttons.destroy()
            
    def rockpaperscissors():
            global variant_text, pcwins, userwins, score
             
            
            if score:
                score.pack_forget()
                
            if variant_text:
                variant_text.pack_forget()
                
            
            variants = ['rock', 'paper', 'scissors']
            variant = random.choice(variants)

            
            
            if rock and variant == "rock":
                variant_text = tk.Label(window,text="TIE!\n rock vs "+variant, background=tie, font=("Arial", 20))
                userwins = userwins + 0
                pcwins = pcwins + 0
                score = tk.Label(window,text="{} : {}".format(userwins, pcwins), background=tie, font=("Arial", 20))
                variant_text.pack()
                score.pack()
                window.configure(background=tie)
                
                
            elif rock and variant == "paper":
                variant_text = tk.Label(window,text="DEFEAT!\n rock vs "+variant, background=defeat, font=("Arial", 20))
                pcwins += 1
                score = tk.Label(window,text="{} : {}".format(userwins, pcwins), background=defeat, font=("Arial", 20))
                variant_text.pack()
                score.pack()
                window.configure(background=defeat)

                
            elif rock and variant == "scissors":
                variant_text = tk.Label(window,text="VICORY!\n rock vs "+variant, background=victory, font=("Arial", 20))
                userwins +=1
                score = tk.Label(window,text="{} : {}".format(userwins, pcwins), background=victory, font=("Arial", 20))
                variant_text.pack()
                score.pack()
                window.configure(background=victory)
                
            elif paper and variant == "rock":
                variant_text = tk.Label(window,text="VICTORY!\n paper vs "+variant, background=victory, font=("Arial", 20))
                userwins += 1
                score = tk.Label(window,text="{} : {}".format(userwins, pcwins), fbackground=victory, font=("Arial", 20))
                variant_text.pack()
                score.pack()
                window.configure(background=victory)
                
            elif paper and variant == "paper":
                variant_text = tk.Label(window,text="TIE!\n paper vs "+variant, background=tie, font=("Arial", 20))
                userwins = userwins + 0
                pcwins = pcwins + 0
                score = tk.Label(window,text="{} : {}".format(userwins, pcwins), background=tie, font=("Arial", 20))
                variant_text.pack()
                score.pack()
                window.configure(background=tie)
                
            elif paper and variant == "scissors":
                variant_text = tk.Label(window,text="DEFEAT!\n paper vs "+variant, background=defeat, font=("Arial", 20))
                pcwins += 1
                score = tk.Label(window,text="{} : {}".format(userwins, pcwins), background=defeat, font=("Arial", 20))
                variant_text.pack()
                score.pack()
                window.configure(background=defeat)
                
            elif scissors and variant == "rock":
                variant_text = tk.Label(window,text="DEFEAT!\n scissors vs "+variant, background=defeat, font=("Arial", 20))
                pcwins += 1
                score = tk.Label(window,text="{} : {}".format(userwins, pcwins), backround=defeat, font=("Arial", 20))
                variant_text.pack()
                score.pack()
                window.configure(background=defeat)
                
            elif scissors and variant == "scissors":
                variant_text = tk.Label(window,text="TIE!\n scissors vs "+variant, background=tie, font=("Arial", 20))
                userwins = userwins + 0
                pcwins = pcwins + 0
                score = tk.Label(window,text="{} : {}".format(userwins, pcwins), background=tie, font=("Arial", 20))
                variant_text.pack()
                score.pack()
                window.configure(background=tie)
            
            elif scissors and variant == "paper":
                variant_text = tk.Label(window,text="VICTORY!\n scissors vs "+variant, background=victory, font=("Arial", 20))
                userwins += 1
                score = tk.Label(window,text="{} : {}".format(userwins, pcwins), background=victory, font=("Arial", 20))
                variant_text.pack()
                score.pack()
                window.configure(background=victory)
                
    defeat = "#FF6969"
    victory = "#06D001"
    tie = "#C7C8CC"       
        
    rock = tk.Button(window, image=rockimage,command=rockpaperscissors)
    rock.pack(pady=50)

    paper = tk.Button(window, image=paperimage,command=rockpaperscissors)
    paper.pack(pady=50)

    scissors = tk.Button(window, image=scissorsimage, command=rockpaperscissors)
    scissors.pack(pady=50)
 
    mainmenu = tk.Button(window, height=5, width=25,text="Main Menu", command=Main)
    mainmenu.pack(padx= 50, pady=0)
 
     
def Main():
    
    for buttons in window.winfo_children():
        buttons.destroy()
        
    mainmenu = tk.Label(window, text="My Games", font=("Arial", 35), background="#77E4C8")
    mainmenu.pack(pady=(35,0))
    
    button1 = tk.Button(window, text="Play Rock, Paper, Scissors!",width=25,height=5, command=RockPaperScissorsGame)
    button1.pack(pady= 85)

    button2 = tk.Button(window,width=25,height=5, text="SOON")
    button2.pack(pady= 85)

    button3 = tk.Button(window,width=25,height=5, text="SOON")
    button3.pack(pady= 85) 

Main()
window.mainloop() #nepretrzita smycka dokud se nezavre okno