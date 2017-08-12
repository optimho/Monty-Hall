import random
# generate three doors, each one with a goat or a car - bu there can only be one car

class Monty_hall:
    """Class to contain the methods to enact the Monty Hall statistical puzzel
    if you select one of three doors and the game show host opens another door to show you a goat
    is it better to keep your selection or swop to the other door
    does this make you 50% likely to succeed or does it give you a better than 50% chance of getting the car prize?
    
    called the Monty Hall problem https://en.wikipedia.org/wiki/Monty_Hall_problem
    
    apparently you should swop to the other door, but I just cant get my head around this.
    
    """
    def __init__(self):
    
        self.door = {"door 1": "test 1", "door 2":"test 2","door 3":"test 3"}
        self.element=["goat","car","goat"]
        self.valid_answers = set([1,2,3])
        self.mydoor_selected=""
        self.show_goat_door=""
        self.wins=0
        self.losses=0
        self._counter=0
        self.history=[]
        self.shuffel()
        
    def shuffel(self):
        
        """shuffels the two goats and one car randomly
            Automatically runs in the __init__ section"""
        
        self.complete =False
        while not self.complete:
            self.random_list_item = 0
            random.shuffle(self.element)
            for self.item in self.door:
                self.door[self.item]=self.element[self.random_list_item]
                self.random_list_item = self.random_list_item +1
                #print(random_list_item)
                #if random_list_item == 2:
            self.complete =True
            
    def get_input(self, num):
        
        """
           Return a selection 
           door 1 - [1]   door 2 - [2] 2   door 3 - [3] 
           
           takes in num which is a real number between 1 and 3
           is_error is True if there is a selection problem.
           
           If there is a selection problem one can test is_error
           and then take appropriate action is the program
           would most likely be a message and re do.
           
           
           
           
           """
        self.is_error=False
 
        while not self.is_error:
            self.choice_num=num
            #print("door 1 - [1]   door 2 - [2] 2   door 3 - [3] ")
            self.line = num
            #print("\n")
            self.item = int(self.line[:1])
            if self.item in self.valid_answers:
                return self.item
        
            elif self.item not in self.valid_answers:
                print ("Input not valid")
                self.is_error=True
    
                self.counter = 0
                self.items=0
                for self.items in self.door:
                    self.counter = self.counter + 1
                    
                if (self.counter == self.selection) :
                    return self.items

   
    def show_me_a_goat(self,exclude):
        
        """show which door has a goat behind it
           but exclude the door that you may have already selected
           """
        self.xcept=exclude
        self.valid_alternative =False
        self.counter = 0

        while not self.valid_alternative:
            self.your_alternative = random.randrange(1, stop=4)
            self.alternative ="door " + str(self.your_alternative)
            #print (door[alternative])
            if self.door[self.alternative]=="goat":
                if self.your_alternative!=self.xcept:
                    #print("true")
                    self.valid_alternative=True  
                    #show_me_a_goat=your_alternative
                    return self.your_alternative
            #print(self.your_alternative)
            
    def which_door_is_closed(self,your_door, the_door_with_the_goat):
        """which door is closed, and available for selection"""
        
        self.set1={your_door, the_door_with_the_goat}
   
        if 'door 1' not in self.set1:
            return 'door 1'
        if 'door 2' not in self.set1:
            return 'door 2'
        if 'door 3' not in self.set1:
            return 'door 3'

    def win_or_loose(self,my_decision,ans,mydoor_selected):
        self._my_decision=my_decision
        self._ans=ans
        self._mydoor_selected=mydoor_selected
        
        if 'keep' in self._my_decision:
            self.gowith=self._mydoor_selected
            print("you choose {}".format(self._mydoor_selected))
        if 'swop' in self._my_decision:
            print("you choose {}".format(self._ans))
            self.gowith=self._ans  
        if 'stop' in self._my_decision:
            self.quit()
    
        if self.door[self.gowith]=="car":
            return "win"
        else:
            return "lose"
    
    
    def get_decision(self, decision):
        """This method processes the selection into a string value
           stop, will be used to exit the program
           keep, will be used to keep ones original selection
           swop, will be used to change ones original selection
           
           decision is a string input ,'k' for keeping the selection
                                      ,'s' for swoping the selection
                                      ,'q' for ending the program """
            
        self.decision=decision
        self.commands=[]           
        #print("keep, [k] to swop, [s] to quit, [q] ")
        self.line = self.decision
        self.command = self.line[:1]

        if self.command =="q":
            self.commands.append("stop")
        elif self.command == "k":
            self.commands.append("keep")
        elif self.command == "s":
            self.commands.append("swop")    

        return self.commands
    
    
    def which_door_is_car(self):
        
        """which door is left closed
           use this function to figure out what door can still be selected """
        
        if 'car' in self.door["door 1"]:
            return 'door 1'
        if 'car' in self.door["door 2"]:
            return 'door 2'
        if 'car' in self.door["door 3"]:
            return 'door 3'    
        
        
    def update_results_log(self, result, selection):
        """a results log
            logs all wins, losses, and has a counter of how many time it iterated
            the log is used for statistical calculations"""
       
        self._result=result
        self._selection = str(selection)
        print (self._selection)
        self._counter=self._counter+1
        self.history.append([self._counter,self._result,self._selection])
      
        
        
    def game_stats_wins_vers_loss(self):
        """returns a percentage of wins versus losses
            =wins/losses
            
            run after some history has been built up"""
        wincount=0
        losscount=0
        ratio=0
        for row in self.history:
            if 'win' in row:
                wincount=wincount+1
            if 'loss' in row:
                losscount=losscount+1
        #print(wincount,losscount)
        
        if wincount>0 and losscount==0:
            losscount=1
        try:
            ratio =(wincount/losscount)*100
            return ratio
        except ValueError:
            print ("Oops!  That was no valid number.  Try again...")
    
    def game_stats_swap(self):    
        """returns a percentage of wins as a percentage
            when one swaps the door that you have selected
            versus losses when you swaped the door selected
            
            =(wins with swop / losses with swop) *100% """
        
        wincount=0
        losscount=0.01
        swap=0
        no_swap=0
        ratio=0
        
        for row in self.history:
            if ('win' in row) and ("'swop'" in row):
                wincount=wincount+1
            if 'loss' in row and "'swop'" in row:
                losscount=losscount+1           
                
        ratio =(wincount/losscount)*100        
        return ratio
    
    def game_stats_no_swap(self):    
        """returns a percentage of wins as a percentage
            when one does not swap the door that you have selected
            versus losses when you dont swap
            
            =(wins with no swop / losses with no swop) *100% """
        
        wincount=0
        losscount=0.01
        swap=0
        no_swap=0
        ratio=0
        
        for row in self.history:
            if 'win' in row and "'keep'" in row:
                wincount=wincount+1
            if 'loss' in row and "'keep'" in row:
                losscount=losscount+1           
                
        ratio =(wincount/losscount)*100        
        return ratio    