import tkinter as tk #importuje knihovnu na okno
import random

        

def RockPaperScissorsGame():
    
    
    
        
    for buttons in window.winfo_children():
            buttons.destroy()
    def rockpaperscissors():
            variants = ['rock', 'paper', 'scissors']
            variant = random.choice(variants)
            variant_text = tk.Label(window, text="")
            variant_text.pack()
            
            
            
            
            if rock and variant == "rock":
                variant_text.config(text="TIE\n rock vs "+variant)
                
                

            
            elif rock and variant == "paper":
                variant_text.config(text="DEFEAT!\n rock vs "+variant)
                

                
            elif rock and variant == "scissors":
                variant_text.config(text="VICORY!\n rock vs "+variant)
                

            elif paper and variant == "rock":
                variant_text.config(text="VICTORY!\n paper vs "+variant)
                
            elif paper and variant == "paper":
                variant_text.config(text="TIE!\n paper vs "+variant)  
                
            elif paper and variant == "scissors":
                variant_text.config(text="DEFEAT!\n paper vs "+variant)
                
            elif scissors and variant == "rock":
                variant_text.config(text="DEFEAT!\n scissors vs "+variant)
                
            elif scissors and variant == "scissors":
                variant_text.config(text="TIE!\n scissors vs "+variant)     
            
            elif scissors and variant == "paper":
                variant_text.config(text="VICTORY!\n scissors vs "+variant)
            
        
    rock = tk.Button(window, text="ROCK", command=rockpaperscissors)
    rock.pack(pady= 65)

    paper = tk.Button(window, text="PAPER", command=rockpaperscissors)
    paper.pack(pady= 75)

    scissors = tk.Button(window, text="SCISSORS", command=rockpaperscissors)
    scissors.pack(pady= 85)
     
    
    
    
        
    
            
            
window = tk.Tk() #vytvori zakladni okno        
window.title("GAMES") #tsitle
window.attributes("-fullscreen", True) #fullscreen


button1 = tk.Button(window, text="Play Rock, Paper, Scissors!", command=RockPaperScissorsGame)
button1.pack(pady= 85)

button2 = tk.Button(window, text="SOON")
button2.pack(pady= 85)

button3 = tk.Button(window, text="SOON")
button3.pack(pady= 85) 






window.mainloop() #nepretrzita smycka dokud se nezavre okno