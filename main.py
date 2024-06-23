import tkinter as tk #importuje knihovnu na okno
import random

score = None       
variant_text = None
pcwins = 0
userwins = 0   
                    
window = tk.Tk() #vytvori zakladni okno        
window.title("GAMES") #tsitle
window.attributes("-fullscreen", True) #fullscreen

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
                variant_text = tk.Label(window,text="TIE!\n rock vs "+variant)
                score = tk.Label(window,text="{} : {}".format(userwins, pcwins))
                variant_text.pack()
                score.pack()
                
                
            elif rock and variant == "paper":
                variant_text = tk.Label(window,text="DEFEAT!\n rock vs "+variant)
                pcwins += 1
                score = tk.Label(window,text="{} : {}".format(userwins, pcwins))
                variant_text.pack()
                score.pack()

                
            elif rock and variant == "scissors":
                variant_text = tk.Label(window,text="VICORY!\n rock vs "+variant)
                userwins +=1
                score = tk.Label(window,text="{} : {}".format(userwins, pcwins))
                variant_text.pack()
                score.pack()
                
            elif paper and variant == "rock":
                variant_text = tk.Label(window,text="VICTORY!\n paper vs "+variant)
                userwins += 1
                score = tk.Label(window,text="{} : {}".format(userwins, pcwins))
                variant_text.pack()
                score.pack()
                
            elif paper and variant == "paper":
                variant_text = tk.Label(window,text="TIE!\n paper vs "+variant)
                score = tk.Label(window,text="{} : {}".format(userwins, pcwins))
                variant_text.pack()
                score.pack()
                
            elif paper and variant == "scissors":
                variant_text = tk.Label(window,text="DEFEAT!\n paper vs "+variant)
                pcwins += 1
                score = tk.Label(window,text="{} : {}".format(userwins, pcwins))
                variant_text.pack()
                score.pack()
                
            elif scissors and variant == "rock":
                variant_text = tk.Label(window,text="DEFEAT!\n scissors vs "+variant)
                pcwins += 1
                score = tk.Label(window,text="{} : {}".format(userwins, pcwins))
                variant_text.pack()
                score.pack()
                
            elif scissors and variant == "scissors":
                variant_text = tk.Label(window,text="TIE!\n scissors vs "+variant)
                score = tk.Label(window,text="{} : {}".format(userwins, pcwins))
                variant_text.pack()
                score.pack()
            
            elif scissors and variant == "paper":
                variant_text = tk.Label(window,text="VICTORY!\n scissors vs "+variant)
                userwins += 1
                score = tk.Label(window,text="{} : {}".format(userwins, pcwins))
                variant_text.pack()
                score.pack()
                
            
        
    rock = tk.Button(window, text="ROCK", command=rockpaperscissors)
    rock.pack(pady= 65)

    paper = tk.Button(window, text="PAPER", command=rockpaperscissors)
    paper.pack(pady= 75)

    scissors = tk.Button(window, text="SCISSORS", command=rockpaperscissors)
    scissors.pack(pady= 85)
     

button1 = tk.Button(window, text="Play Rock, Paper, Scissors!", command=RockPaperScissorsGame)
button1.pack(pady= 85)

button2 = tk.Button(window, text="SOON")
button2.pack(pady= 85)

button3 = tk.Button(window, text="SOON")
button3.pack(pady= 85) 

window.mainloop() #nepretrzita smycka dokud se nezavre okno