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
    def performIncantation(self, incantation):

        # Perform raindance
        if incantation.lower()=='raindance':

            # Print display
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

        else:

            print("That incantation isn't in this book!")


    def howToUseMethodByName(self,funcName):#TODO

        pass




class House:

    def __init__(self):

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

        self._fireStartedAt = None
        self._roomnames = ['Kitchen', 'Bathroom', 'Living Room', 'Basement', 'Kennel', 'Attic', 'Bedroom', 'Study', 'ChamberOfDeath']
        self._roomindex = roomindex
        self._burnedOut = False
        self._foundBook = False
        self._foundKey = False
        self._foundDog = False
        self._foundKid = False
        self._triedValve = False
        self.activateSprinklerSystem = False


    def __repr__(self):
        
        return('House')

    def howToUseMethodByName(self,funcName):#TODO

        self.__check__()

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


    def burnToGround(self):

        if not self._fireStartedAt:
            self._fireStartedAt = time.time()
        print('Yup. The house is now on fire. Great job.')

    def listRooms(self):

        self.__check__()
        return self._roomnames

    def roomDescription(self, roomName): 

        self.__check__()

        if time.time()-self._fireStartedAt >= 1000:

            self._burnedOut = True

            raise ValueError('The house burned down... damn.')

        if roomName.lower() in ['kitchen', 'bathroom', 'living room', 'basement', 'attic', 'bedroom', 'study']:

            print('Nothing of interest to report.')
            return(0)

        elif roomName.lower()=='kennel':

            print('It says the name "Spike" on the wall... I wonder if this information could be useful somewhere else...')
            return(0)

        elif roomName.lower()=='chamberofdeath':

            print('A big concrete chamber... weird symbols on the walls... cold... so cold... I doubt this place will burn down anytime soon...')
            time.sleep(1)
            print(" ")
            time.sleep(1)
            print("Hey wait! What's this?! A weird mystical book! Maybe you should keep hold of this... I'd save the result of this function call if I were you!")
            time.sleep(1)
            print(" ")
            time.sleep(1)
            print("Ah the fumes are coming in!!! You've only got " + str(1000-(time.time()-self._fireStartedAt)) + " seconds until the whole place goes up in flames!!")
            time.sleep(1)
            print(" ")
            time.sleep(1)
            print("I wonder if this mystical book has any useful methods...")
            return(mysticalBook())

        else: 

            print("Invalid room name.")


    def isItemInRoom(self, itemName, roomName): #TODO

        self.__check__()

        if itemName.lower() == 'dog' and not self._foundDog:

            print("Which Dog? Need to be more specific...")
            time.sleep(1)
            print(" ")
            time.sleep(1)
            print("Tic toc tic toc! Fires spreading...")
            time.sleep(1)
            print(" ")
            time.sleep(1)
            print("Maybe there's a clue *described* somewhere!")

        elif itemName.lower() == 'spike' and not self._foundDog:

            roomNo = (time.time()//10 % 9)

            if self._roomindex[roomNo].lower()==roomName.lower():

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
                self._foundDog = True

            else:

                print("The dogs not in here!")
                time.sleep(1)
                print(" ")
                time.sleep(1)
                print("Times running down!! Keep looking!!")
                time.sleep(1)
                print(" ")
                time.sleep(1)
                print("He's probably moving around a lot in the fire! He might be here in a minute!")


        elif itemName.lower() == 'valve':

            if roomName.lower() == 'bedroom':

                if self._foundKey:

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

                    if not self._foundBook:
                        print("Did you check out all of the rooms?! Things are getting real bad here... maybe something about the chamber of death can help... if only you knew how to do a 'raindance' ;)")
                    else:
                        print("Last hope!! Did you find anything (potentially book-shaped) recently?! Maybe it can help you to perform... a 'raindance' ;)")

                else:

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

                self._triedValve = True

            else:

                print('Nope, no valve here!')

        elif itemName.lower() == 'kid' and not self._foundKid:

            roomNo = (time.time()//20 % 9)

            if self._roomindex[roomNo].lower()==roomName.lower():

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
                if self._triedValve:
                    print("That damn kid! He's got the key to the padlock for that valve! Kids, eh? Best try the valve again (rerun the same command as last time!)!")
                else:
                    print("Huh the kids got a key... what's this for?")
                self._foundKey = True
                self._foundKid = True

            else:

                print("That damn kid! He's not in here at the moment!! Keep looking!!")

        elif itemName.lower() == 'cucumber':

            if roomName.lower() == 'kitchen':

                print('Yup. Well done. The house is on fire but you found a Cucumber. Great work.')

            elif roomName.lower() == 'chamberofdeath':

                print('Why would there be a cucumber in the chamber of death?')

            else:

                print('Why would there be a cucumber in the ' + roomName.lower() + '?')


        elif self._foundKid:

            print("You already found the kid, no?")

        elif self._foundDog:

            print("You already found the dog, no?")

        else: 

            print("Invalid room/item combination.")

    def __check__(self):

        if self._fireStartedAt:

            if time.time()-self._fireStartedAt >= 1000:

                self._burnedOut = True

            if self._burnedOut:

                raise ValueError('The house burned down... damn.')

    def status(self):

        if self._fireStartedAt:

            if time.time()-self._fireStartedAt >= 1000:

                self._burnedOut = True

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
                print("You've only got " + str(1000-(time.time()-self._fireStartedAt)) + " seconds left!!! Get a move on!")

            if self._burnedOut:

                raise ValueError('The house burned down... damn.')

        else:

            print('The house is not on fire!')

    def turnOnSprinklers(self):

        self.__check__()

        if self._fireStartedAt and not self.activateSprinklerSystem:

            print("The sprinklers aren't working... You'll have to turn on the water on manually!")
            time.sleep(1)
            print(" ")
            time.sleep(1)
            print("You might have to work out which room the sprinkler 'Valve' is in... If only there were some useful code given to you earlier in the notebook!")
            time.sleep(1)
            print(" ")
            time.sleep(1)
            print('Time until total house annihilation: ', str(1000-(time.time()-self._fireStartedAt)), ' seconds and counting.')
            time.sleep(1)
            print(" ")
            time.sleep(1)
            print('Hint: The method starting "howToUse..." might help if you feed it the names of other methods.')

        elif self.activateSprinklerSystem:

            print("There's a creak...")
            time.sleep(1)
            print(" ")
            time.sleep(1)
            print("Only " + str(1000-(time.time()-self._fireStartedAt)) + " seconds left")
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

            self._fireStartedAt = False

        else:

            print("Why are you turning the sprinklers on? There's no fire here!")