"""
Isabelle Dweidary
Assignment 10.1 - Your Own Class
Acknowledgements:
Hari's Lectures
"""

# import random and time modules
import random
import time

# Fishing Class
class Fishing:
    # initializing place class variable
    place = ""
    # init function that takes in self, a fish_goal, and a weight_goal
    def __init__(self, fish_goal, weight_goal):
        # intialize a lot of data variables
        self.__fishgoal = fish_goal
        self.__weightgoal = weight_goal
        self.__location = 0
        self.__total_fish = 0
        self.__total_caught = 0
        self.__total_weight = 0
        self.__tackle_box = []

    # this method is used to set the location where you want to fish. There are 3 locations.
    def set_location(self, location_number):
        # initialize variable
        self.__location = location_number
        # if the location is 1: return a statement saying they are location at the ocean
        if self.__location == 1:
            self.__place = "The Ocean"
            return(print(f"You set your location to location {self.__location}: The Ocean"))
        # if the location is 2: return a statement saying they are location at the river
        elif self.__location == 2: 
            self.__place = "The River"
            return (print(f"You set your location to location {self.__location}: The River"))
        # if the location is 3: return a statement saying they are location at freshwater
        elif self.__location == 3:
            self.__place = "Freshwater"
            return (print(f"You set your location to location {self.__location}: Freshwater"))
        # if they input a number that is less than one or more than 3
        elif self.__location < 1 or self.__location > 3: 
            # raise an error saying they need to choose a specified location number 
            raise IndexError("Please choose a location between 1 and 3.")

    # method for actually fishing
    def fish(self):
        # this is the fish you can catch
        fish_list = ["Salmon", "Tuna", "Shark", "Stingray", "Jellyfish", "Starfish"]
        # this is the random chance for your strength
        self.__catch_chance = random.randint(0, 10)
        # this is the random chance for your weight
        self.__random_weight = random.randint(1, 4) 
        # this is random fish you catch from the list
        self.__fish_caught = random.choice(fish_list)
        # if there are no fish in the location, print no fish here
        if self.__total_fish == 0:
            print("There are no fish in this location :(")
            # then break out
            return
        # otherwise, if your strength roll is over 5, you catch the fish and print a couple messages
        if self.__catch_chance > 5:
            print(f"You caught the fish! It was a {self.__fish_caught}")
            print(f"You had {self.__catch_chance} out of 10 power.")
            print(f"It has a weight of {self.__random_weight}.")
            # add 1 to total caught and add random weight to total weight
            self.__total_caught += 1
            self.__total_weight += self.__random_weight
            # append the fish to your tackle box 
            self.__tackle_box.append(self.__fish_caught)
        # if your strength roll is less than or equal to 5, print the fish got away 
        elif self.__catch_chance <= 5:
            print(f"The fish got away :(. You had a {self.__catch_chance} out of 10 power.")

    # method for checking what is inside your tackle box
    def check_tackle(self):
        return(print(f"Stored in your tackle box: {self.__tackle_box}"))

    # method for getting how many fish in one location
    def get_total_fish_in_location(self):
        # generate a random number of fish between 0 and 2 
        self.__total_fish = random.randint(0, 5)
        # then return the amount of fish in a print statement 
        return(print(f"The total amount of fish in {self.__place} is {self.__total_fish}"))
    
    # method for checking what your goal is
    def goal_check(self):
        # first print their fish goal compared to their total amount of fish caught
        print(f"Your total fish goal is {self.__fishgoal} and you have caught {self.__total_caught} total.")
        time.sleep(2)
        # then print their weight goal compared to their total weight aquired
        print(f"Your total weight goal is {self.__weightgoal} and you have {self.__total_weight} weight total.")

    # method for returning total caught value
    def get_total_caught(self):
        return(self.__total_caught)
    
    # method for returning total weight value
    def get_total_weight(self):
        return(self.__total_weight)

    # method for returning fish goal
    def get_fish_goal(self):
        return(self.__fishgoal)
    
    # method for returning weight goal
    def get_weight_goal(self):
        return(self.__weightgoal)


# main function testing fishing class
def main():
    # call the class with a random fish goal of between 2 and 6 fish
    # and a random weight goal between 5 and 12
    x = Fishing(random.randint(2, 6), random.randint(5, 12))
    # while total caught weight is less than weight goal or total fish caught is less than fish goal execute loop
    while x.get_total_weight() < x.get_weight_goal() or x.get_total_caught() < x.get_fish_goal():
        # use set_location method to generate a random location between 1 and 3 
        x.set_location(random.randint(1, 3))
        # all sleep timers are meant to make the fishing seem more realistic 
        time.sleep(2)
        # this uses get_total_fish_in_location method to print the amount of fish in the location you're fishing at
        x.get_total_fish_in_location()
        time.sleep(2)
        # this is the fish method. It will try and catch a fish if there is one and you roll a 5 or higher in the method
        x.fish()
        time.sleep(2)
        # this method prints what fish you have in your tackle box 
        x.check_tackle()
        time.sleep(2)
        # this will compare the fish you caught and their weights with the goals 
        x.goal_check()
        time.sleep(2)
    # when you reach both of the goals, a congratulations message is printed
    print(f"You reached both of your goals! Congratulations! Your haul {x.check_tackle()}")


# calling the main function
if __name__ == "__main__":
    main()