# Monty-Hall
simulates the Monty hall puzzel and proves the concept.
https://en.wikipedia.org/wiki/Monty_Hall_problem

Simply put it is a puzzel that displays our in numeracy.
It was a game show where you would pick one of three doors that you think the car is located, the game show host would then open one of the doors to reveal a goat
then ask you it you were still comfortable with your choice. Instincively, you would think that you have a 50/50 chance, but change to the other door
and you would actually be increasing your odds by a factor of three!
This program can run in two modes auto=True and auto=False (note the capitals)
In auto = True, the computer makes random choices for you and can quickly grows a sizable data sample
In auto = False you have to make all the entries.
the program has a Monty Hall class and an example python program that incorporates the class as an example.
the update_results_log method is called to update a loss or a win as well as what the decision was and stores it in a list along with an
iteration counter
the game_stats_swap and game_stats_no_swap are two methods that are called after every couple hunderd iterations.
The methods read the list of the stored log and calculates how many times one has won, when there was a swop. The other method does the 
same but calculates the number of wins as a percent, to the number of times one HAS swoped!

There is alot of room to expand and improve the code.
But it more than confirms the probability laws -In this case, you win 2 (200%) x more if you swop every time, or you will 
win half (50%) as many times as you lose if you do not swop.

Most sources say that you should win 2/3 (66%) of the time if you swop and 1/3 (33%) if you do not swop.
You should be able to glean this information by adding a method to calculate (wins/iterations) * 100%  and another for (losses/iteration) *100%
