
import time
import random
import Monty_hall

game1=Monty_hall.Monty_hall()
swop_or_no_swop=['k','s']
loop_count=0


while 1:
    
    auto=True #Select for manual or auto mode
    game1.shuffel()
    #print(game1.door)
    
    ##################################################
    #Select a door
    ##################################################
    if (not auto):#man mode
        print("door 1 - [1]   door 2 - [2] 2   door 3 - [3] ")
        num=input()
    if auto:
        num=str(random.randrange(1, stop=4) )   
    your_choice=game1.get_input(num)    
    mydoor_selected="door " + str (your_choice) 
    
    if (not auto):#man mode
        print("You choose", mydoor_selected)
        
   ####################################################
   # Open a door and show you a goat
   ####################################################
    show_goat_door=game1.show_me_a_goat(your_choice)
    if (not auto):
        print("There is a goat behind door", show_goat_door)

    goatdoor_selected="door " + str (show_goat_door) 
   ####################################################

    ####################################################
    #Which door is still closed?
    ####################################################
    ans=game1.which_door_is_closed(mydoor_selected, goatdoor_selected)
    if (not auto):#man mode
        print ("door that is still closed is",ans)   
        
        
    ####################################################
    #decisio to change or stay
    ####################################################    
    
    if (not auto): #man mode
        print("do you want to keep {} or change to {}".format(mydoor_selected, ans))
        print("keep, [k] to swop, [s] to quit, [q] ")
        my_decision=game1.get_decision(input())
        my_decision=str(my_decision).replace('[','').replace(']','')
        print()
        
        
    ####################################################
    #decision to change or stay auto mode
    ####################################################         
    if auto:
        
        my_decision=game1.get_decision(str(swop_or_no_swop[random.randrange(0, stop=2)]))
        #print((my_decision))
        my_decision=str(my_decision).replace('[','').replace(']','')
        #print()        
        
        ####################################################
        #where is the car? display in manual mode
        ####################################################     
    
    if  (not auto):#man mode
        print ("The car is behind ", game1.which_door_is_car())
        
        
        ####################################################
        #update the log with the wins and losses
        ####################################################     
    
    if game1.win_or_loose(my_decision,ans,mydoor_selected)=='win':
        game1.wins=game1.wins+1
        game1.update_results_log('win', my_decision)
    else:
        game1.losses=game1.losses+1
        game1.update_results_log('loss', my_decision)
        
        ####################################################
        #display the amount of wins and losses
        ####################################################     
    if (not auto) or auto:#man mode or auto mode
        print ("wins {}" .format(game1.wins))
        print ("losses {}".format (game1.losses))
        
        
        ####################################################
        #game stst section 
        ####################################################
        
        # stats games won versus lost
   # game1.game_stats_wins_vers_loss()
    
        # every 100 iterations calculate statistics
    loop_count=loop_count+1
    if loop_count==1000:
        #wins versus losses if you swop 
        print ("% wins to losses when you swop ", game1.game_stats_swap())
        #wins versus losses if you do not swop
        print ("% wins to losses when you do not swop", game1.game_stats_no_swap())
        #print ("% wins if you swop vers if you do not swop ", 100*(game1.game_stats_swap()/game1.game_stats_no_swap())
        time.sleep(2)    
        loop_count=0
        
    




