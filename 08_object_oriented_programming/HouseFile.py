import time
import numpy as np

# Class for the mystical book found in the chamber of death.
class mysticalBook:

    # Init method
    def __init__(self):

        pass

    # Represent method
    def __repr__(self):
        
        return('MysticalBook')

    # Perform incantation method.
    def performIncantation(self, incantation): #TODO

        # Run incantation
        if incantation.lower()=='raindance':

            # Display text
            print("Things are getting more desperate than they've ever been...")
            time.sleep(2.5)
            print(" ")
            time.sleep(2.5)
            print("You climb up the stairs...")
            time.sleep(2.5)
            print(" ")
            time.sleep(2.5)
            print("The smoke fumes are making you dizzy...")
            time.sleep(2.5)
            print(" ")
            time.sleep(2.5)
            print("All you wanted to do was learn object oriented programming but now you're an arsonist, a dog hunter and now this...")
            time.sleep(2.5)
            print(" ")
            time.sleep(2.5)
            print("You break a hole in the attic roof! How did things come to this?! You curse your gods and rue the day you chose to learn Python!")
            time.sleep(2.5)
            print(" ")
            time.sleep(2.5)
            print("It's a cold, cold chilly night. You think of the dog and the kid.")
            time.sleep(2.5)
            print(" ")
            time.sleep(2.5)
            print("Oh how you wish it was ten minutes ago when your biggest worry in life was what the 'self' argument meant!")
            time.sleep(2.5)
            print(" ")
            time.sleep(2.5)
            print("You raise your arms to the sky...")
            time.sleep(2.5)
            print(" ")
            time.sleep(2.5)
            print("You take a deep breath... ")
            time.sleep(2.5)
            print(" ")
            time.sleep(2.5)
            print("... and perform a raindance!")
            time.sleep(2.5)
            print(" ")
            time.sleep(2.5)
            print("Silence.")
            time.sleep(2.5)
            print(" ")
            time.sleep(2.5)
            print("You moron. Did you really think that would work?!")
            time.sleep(2.5)
            print(" ")
            time.sleep(2.5)
            print('Wait...')
            time.sleep(2.5)
            print(" ")
            time.sleep(2.5)
            print('You moron!! You just remembered!')
            time.sleep(2.5)
            print(" ")
            time.sleep(2.5)
            print("Did you turn the 'activateSprinklerSystem' boolean attribute on in the house?!")
            time.sleep(2.5)
            print(" ")
            time.sleep(2.5)
            print("Quick go back and try this and turn on the sprinklers again!!")

        # Unknown incantation
        else:
            print("That incantation isn't in this book!")


    # Documenting function
    def howToUseMethodByName(self,funcName):

        # Document book functions
        if funcName=='performIncantation':
            print("Run like this: performIncantation(incantation) where incantation is a string representing the kind of incantation you want to run!")
        else:
            print("Function name not recognized!")


# Class for house
class House:

    # Initialize house
    def __init__(self):

        # List of rooms
        roomindex = dict()
        roomindex[0]='Kitchen'
        roomindex[1]='Bathroom'
        roomindex[2]='Living Room'
        roomindex[3]='Basement'
        roomindex[4]='Kennel'
        roomindex[5]='Attic'
        roomindex[6]='Bedroom'
        roomindex[7]='Study'
        roomindex[8]='ChamberOfDeath'

        # Initial variables
        self.__fireStartedAt = None
        self.__roomnames = ['Kitchen', 'Bathroom', 'Living Room', 'Basement', 'Kennel', 'Attic', 'Bedroom', 'Study', 'ChamberOfDeath']
        self.__roomindex = roomindex
        self.__burnedOut = False
        self.__foundBook = False
        self.__foundKey = False
        self.__foundDog = False
        self.__foundKid = False
        self.__triedValve = False
        self.activateSprinklerSystem = False

    # Represent function
    def __repr__(self):
        
        # Return house as string
        return('House')

    # Key for how to use methods
    def howToUseMethodByName(self,funcName):#TODO

        # Check if house has burned down yet
        self.__check__()

        # List functions
        if funcName=='burnToGround':
            print("I think you're already familiar enough with this one, aren't you?")
        elif funcName=='listRooms':
            print("Just call it like 'roomlist=house.listRooms()'!")
        elif funcName=='roomDescription':
            print("Pass it a string representing a room name; e.g. 'house.roomDescription('Attic')'")
        elif funcName=='isItemInRoom':
            print("Pass strings representing an item name and a room name; e.g. 'house.isItemInRoom('Cucumber','Attic')'")
        elif funcName=='status':
            print("Just call it like 'house.status()'!")
        elif funcName=='turnOnSprinklers':
            print("Just call it like 'house.turnOnSprinklers()'!")
        elif funcName=='howToUseMethodByName':
            print("Think you've already got this one covered!")
        elif funcName.contains('_'):
            print("Don't worry about this function!")
        else:
            print("Function name not recognized!")

    # Burn house to the ground
    def burnToGround(self):

        # If we've not set the fire, start it. 
        if not self.__fireStartedAt:
            self.__fireStartedAt = time.time()

        # Tell the user.
        print('Yup. The house is now on fire. Great job.')

    # List the rooms in the house.
    def listRooms(self):

        # Check if the house is burned down yet.
        self.__check__()

        # return the roomnames
        return self.__roomnames

    # Function to describe the rooms
    def roomDescription(self, roomName): 

        # Check if the house is burned down yet.
        self.__check__()

        # Rooms of no interest
        if roomName.lower() in ['kitchen', 'bathroom', 'living room', 'basement', 'attic', 'bedroom', 'study']:

            print('Nothing of interest to report.')
            return(0)

        # Kennel, for dogs name
        elif roomName.lower()=='kennel':

            print('It says the name "Spike" on the wall... I wonder if this information could be useful somewhere else...')
            return(0)

        # Chamber of death, for book
        elif roomName.lower()=='chamberofdeath':

            # Describe
            print('A big concrete chamber... weird symbols on the walls... cold... so cold... I doubt this place will burn down anytime soon...')
            time.sleep(1)
            print(" ")
            time.sleep(1)
            print("Hey wait! What's this?! A weird mystical book! Maybe you should keep hold of this... I'd save the result of this function call if I were you (e.g. `book=roomDescription('ChamberOfDeath')`)!")
            time.sleep(1)
            print(" ")
            time.sleep(1)
            print("Ah the fumes are coming in!!! You've only got " + str(1000-(time.time()-self.__fireStartedAt)) + " seconds until the whole place goes up in flames!!")
            time.sleep(1)
            print(" ")
            time.sleep(1)
            print("I wonder if this mystical book has any useful methods...")

            # Return book
            return(mysticalBook())

        # Unknown room name
        else: 

            print("Invalid room name.")

    # Check if an item is in a room
    def isItemInRoom(self, itemName, roomName):

        # Check if the house is burned down yet.
        self.__check__()

        # Check if we're looking for the dog
        if itemName.lower() == 'dog' and not self.__foundDog:

            # Tell the user to go look for dogs name
            print("Which Dog? Need to be more specific...")
            time.sleep(1)
            print(" ")
            time.sleep(1)
            print("Tic toc tic toc! Fires spreading...")
            time.sleep(1)
            print(" ")
            time.sleep(1)
            print("Maybe there's a clue *described* somewhere!")

        # Check for spike the dog
        elif itemName.lower() == 'spike' and not self.__foundDog:

            # Generate room number spike is in based on time code.
            roomNo = (time.time()//10 % 9)

            # Check if spikes in the room!
            if self.__roomindex[roomNo].lower()==roomName.lower():

                # They caught spike!
                print("You caught the dog!")
                time.sleep(1)
                print(" ")
                time.sleep(1)
                print("Great let's get out of th.... Wait... crap! ")
                time.sleep(1)
                print(" ")
                time.sleep(1)
                print("What about the kid?! ")
                time.sleep(1)
                print(" ")
                time.sleep(1)
                print("You can't leave the 'kid' in the house! Better find him quick!")

                # Set found dog to true
                self.__foundDog = True

            # They didn't catch him
            else:

                # Tell the user.
                print("The dogs not in here!")
                time.sleep(1)
                print(" ")
                time.sleep(1)
                print("Times running down!! Keep looking!!")
                time.sleep(1)
                print(" ")
                time.sleep(1)
                print("He's probably moving around a lot in the fire! He might be here in a minute!")

        # Check if the valves in the room
        elif itemName.lower() == 'valve':

            # Check if looking at bedroom
            if roomName.lower() == 'bedroom':

                # Already found the valve
                if self.__foundKey:

                    # Unlock the valve
                    print("Unlocking the padlock on the valve with the kids key...")
                    time.sleep(1)
                    print(" ")
                    time.sleep(1)
                    print("Turning valve...")
                    time.sleep(1)
                    print(" ")
                    time.sleep(1)
                    print("Come onnnn...")
                    time.sleep(1)
                    print(" ")
                    time.sleep(1)
                    print("It's on!!")
                    time.sleep(1)
                    print(" ")
                    time.sleep(1)
                    print("WAIT!")
                    time.sleep(1)
                    print(" ")
                    time.sleep(1)
                    print("NOTHINGS HAPPENING!")
                    time.sleep(1)
                    print(" ")
                    time.sleep(1)
                    print('THE FIRES SPEEDING UP!!')
                    time.sleep(1)
                    print(" ")
                    time.sleep(1)
                    print('Things are getting desperate!!') 
                    time.sleep(1)
                    print(" ")
                    time.sleep(1)

                    # Check if already found the book
                    if not self.__foundBook:
                        print("Did you check out all of the rooms?! Things are getting real bad here... maybe something about the chamber of death can help... if only you knew how to do a 'raindance' ;)")
                    else:
                        print("Last hope!! Did you find anything (potentially book-shaped) recently?! Maybe it can help you to perform... a 'raindance' ;)")

                # Otherwise, finding valve for first time
                else:

                    # Tell user to find the dog
                    print("Why would anyone ever put a sprinkler valve in a bedro... Wait! Wtf?! It's here!!")
                    time.sleep(1)
                    print(" ")
                    time.sleep(1)
                    print("Ah crap! The valves been chained up!")
                    time.sleep(1)
                    print(" ")
                    time.sleep(1)
                    print("Right...")
                    time.sleep(1)
                    print(" ")
                    time.sleep(1)
                    print("Let's give up on that and get to safety!")
                    time.sleep(1)
                    print(" ")
                    time.sleep(1)
                    print("You should find your 'dog' and get out of the house ASAP!!")

                # Record that we've tried the valve now
                self.__triedValve = True

            # The valve isn't in any other room
            else:
                print('Nope, no valve here!')

        # Find the kid
        elif itemName.lower() == 'kid' and not self.__foundKid:

            # Generate a room for the kid to be in
            roomNo = (time.time()//20 % 9)

            # They found the kid.
            if self.__roomindex[roomNo].lower()==roomName.lower():

                # Tell the user they found the kid and key
                print('You found the kid!')
                time.sleep(1)
                print(" ")
                time.sleep(1)
                print('Man the flames are getting pretty bad now though...')
                time.sleep(1)
                print(" ")
                time.sleep(1)
                print('Things are starting to get a bit desperate here... Better get out of here!')
                time.sleep(1)
                print(" ")
                time.sleep(1)
                print('Wait!')
                time.sleep(1)
                print(" ")
                time.sleep(1)
                if self.__triedValve:
                    print("That damn kid! He's got the key to the padlock for that valve! Kids, eh? Best try the valve again (rerun the same command as last time!)!")
                else:
                    print("Huh the kids got a key... what's this for?")

                # Record found the key and kid
                self.__foundKey = True
                self.__foundKid = True

            # Otherwise, tell the user they haven't found him
            else:
                print("That damn kid! He's not in here at the moment!! Keep looking!!")

        # Cucumber was example
        elif itemName.lower() == 'cucumber':

            # Sarcasm, obviously
            if roomName.lower() == 'kitchen':
                print('Yup. Well done. The house is on fire but you found a Cucumber. Great work.')

            # 
            elif roomName.lower() == 'chamberofdeath':

                print('Why would there be a cucumber in the chamber of death?')

            else:

                print('Why would there be a cucumber in the ' + roomName.lower() + '?')


        elif self.__foundKid:

            print("You already found the kid, no?")

        elif self.__foundDog:

            print("You already found the dog, no?")

        else: 

            print("Invalid room/item combination.")

    def __check__(self):

        if self.__fireStartedAt:

            if time.time()-self.__fireStartedAt >= 1000:

                self.__burnedOut = True

            if self.__burnedOut:

                raise ValueError('The house burned down... damn.')

    def status(self):

        if self.__fireStartedAt:

            if time.time()-self.__fireStartedAt >= 1000:

                self.__burnedOut = True

            else:

                randNo = np.random.uniform()
                if randNo < 0.1:
                    print("It's getting pretty smokey...")
                elif randNo < 0.2:
                    print("Flames licking the walls now!")
                elif randNo < 0.3:
                    print("Let's just say the insurance isn't looking hopeful...")
                elif randNo < 0.4:
                    print("Well... I guess they say some like it hot...")
                elif randNo < 0.5:
                    print("To say things were going well would certainly be a... hot take!")
                elif randNo < 0.6:
                    print("Yeah... you might want to get a move on!!")
                elif randNo < 0.7:
                    print("Kasabian rang. They asked if they could use this incident for song inspiration.")
                elif randNo < 0.8:
                    print("Well, on the plus side you can turn the heating off.")
                elif randNo < 0.9:
                    print("Tic Toc Tic Toc. Fires pretty bad now!")
                else:
                    print('Yup. Still on fire!')

                time.sleep(1)
                print(" ")
                time.sleep(1)
                print("You've only got " + str(1000-(time.time()-self.__fireStartedAt)) + " seconds left!!! Get a move on!")

            if self.__burnedOut:

                raise ValueError('The house burned down... damn.')

        else:

            print('The house is not on fire!')

    def turnOnSprinklers(self):

        self.__check__()

        if self.__fireStartedAt and not self.activateSprinklerSystem:

            print("The sprinklers aren't working... You'll have to turn on the water on manually!")
            time.sleep(1)
            print(" ")
            time.sleep(1)
            print("You might have to work out which room the sprinkler 'Valve' is in... If only there were some useful code given to you earlier in the notebook!")
            time.sleep(1)
            print(" ")
            time.sleep(1)
            print('Time until total house annihilation: ', str(1000-(time.time()-self.__fireStartedAt)), ' seconds and counting.')
            time.sleep(1)
            print(" ")
            time.sleep(1)
            print('Hint: The method starting "howToUse..." might help if you feed it the names of other methods.')

        elif self.activateSprinklerSystem:

            print("There's a creak...")
            time.sleep(1)
            print(" ")
            time.sleep(1)
            print("Only " + str(1000-(time.time()-self.__fireStartedAt)) + " seconds left")
            time.sleep(1)
            print(" ")
            time.sleep(1)
            print("But the sprinklers come on!")
            time.sleep(1)
            print(" ")
            time.sleep(1)
            print("Phew!")
            time.sleep(1)
            print(" ")
            time.sleep(1)
            print("The fire is out! Well done!")
            time.sleep(1)
            print(" ")
            time.sleep(1)
            print("I guess it's time to go back to some object oriented programming, huh?")

            self.__fireStartedAt = False

        else:

            print("Why are you turning the sprinklers on? There's no fire here!")