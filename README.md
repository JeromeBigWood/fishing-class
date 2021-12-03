# fishing-class
a class and demo program for fishing written in python

Class Documentation

Description of class: 

The Fishing class was made with the purpose of modeling the ideal fishing experience. The class allows you to chose different locations to fish in, spawns fish in randomly mimicing the real world, generates strength factor which decides whether or not you are able to catch the fish, and puts it into your tacklebox if you do. It is meant to create an immersive experience that reminds the user of fishing in real life. 

Description of class variables:

"place": I use this to store the location that the user spawns into. 

"fish_list": This is used to store all the different kinds of fish that can be caught.

Description of data variables: 

"self.__fishgoal" is used to store the goal of fish needed to be caught.

"self.__weightgoal" is used to store the goal of fish weight needed to be aquired.

"self.__location" is used to store the location number, ranging from one to three. 

"self.__total_fish" is used to store the amount of fish that reside in one location.

"self.__total_caught" is used to store the total amount of fish that have been caught by the user. 

"self.__total_weight" is used to store the total amount of weight from fish that have been caught by the user. 

"self.__tackle_box" is used to store the names of all of the different kinds of fish that the user catches in one trip.

"self.__catch_chance" is used to store the strength value for being able to reel in a fish.

"self.__random_weight" is used to store the random value generated for the weight of the fish caught. 

"self.__fish_caught" is used to store the string value for the name of the fish caught. 

Description of methods: 

"set_location" is used to set the location of where you want to fish based on an argument that is supported by an input of 1-3. The return based on which location chosen will print a statement saying you are at said location. If a number below 1 or above 3 is inputted, it will raise an IndexError promping the user to input a number between 1 and 3. 

"fish" is the method I used to actually make the fishing happen. First the function generates a random number which is the strength to catch the fish. A strength above 5 is needed to catch the fish. Then it generates a number between 1 and 3 which is the weight of the fish. If your strength is enough, then it prints out a congratulations message saying you caught the fish and what type of fish it was as well as the power you used to catch the fish. Then it adds one to tthe total amount of fish caught and adds the random weight that was generated to your total weight caught. If strength is less than 5, the user is prompted a message that says that the fish got away. 

"check_tackle" is a simple method used to get the list of fish in your tackle box. It will display a list that has all current fish that have been caught.

"get_total_fish_in_location" is used to generate a number of fish between 0 and 5 in one location. Then it will print a message saying in that location there are a specific amount of fish living there. 

"goal_check" is used to print what the goal for fish caught is and the total currently caught. It also prints the weight goal and the current weight acquired. 

"get_total_caught" is a way to return the value for total amount of fish caught.

"get_total_weight" is a way to return the value for total weight from fish acquired.

"get_fish_goal" is a way to return the fish goal that was initially set.

"get_weight_goal" is a way to return the fish weight goal that was intially set. 


Demo Program Documentation: 

Description of demo program: 

My demo program is a representation of what a fishing trip should look like. It first calls the class with randomly generated parameters for the fish goal and the weight goal. Then it enters a while loop until both of your goals are reached. First it sets the location where you want to fish. Then it generates the amount of fish in that locaiton. After that, if there are fish, it will generate a random number through the fish function to check if you are strong enough to catch it. If you are, you add the fish and the weight to the current stats, if not the fish gets away and you fish again. After running the fish function, I have it check what is inside of the tackle box. Finally, the goal is checked to see if you reached it. If so, the program is ended with a congratulations message. 

How to run demo program:

The program is pretty much self sufficient, so you would just need open your terminal and type "python3" followed by the filename to run it. The filename I used is custom_class.py. 
