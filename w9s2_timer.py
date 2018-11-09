from w9s1_counter import *
# Now we create a timer class.
# Our timer should keep track of some amount of hours, minutes, and seconds.
# When we ask the timer to tick, the seconds value should always decrease.
# If we went from 0 to 59 seconds being displayed, we should decrease minutes
# If we went from 0 to 59 minutes being displayed, we should decrease hours

# Finally, we should be able to tell that the timer is done.

class Timer:
    # As usual, begin with the constructor.
    # In this case, we want our timer to be made up of 3 numbers, but which behave like the counters we created.
    # This means that a timer is made up of 3 counters.
    def __init__(self, initial_hours, initial_minutes, initial_seconds):
        self.hours = Counter(initial_hours, 23)# Loop at 23, although we want use that in this case.
        self.minutes = Counter(initial_minutes, 59)# Loop at 59, as there are 60 minutes in an hour
        self.seconds = Counter(initial_seconds, 59)# Loop at 59, as there are 60 seconds in a minute

    # How should we display the timer?
    def __str__(self):
        # Note here we use str(self.hours), where self.hours is a Counter object.
        # This means that we want to convert a counter to a String
        # Therefore, this will use the __str__ method in the Counter Class to convert hours, minutes, and seconds
        # and concatenate a bigger string for our timer.
        return "The current timer is " + str(self.hours) + ":" + str(self.minutes) + ":" + str(self.seconds)

    # The timer is over if each counter's current value is 0, indicating that we have 0 hours, minutes, and seconds left
    # This will return a boolean
    def is_over(self):
        return self.hours.current_value == 0 and self.minutes.current_value == 0 and self.seconds.current_value == 0

    # Note here that even if this method is called tick(), python is not confused.
    # Remember that the pattern for calling methods is object_name.method_name()
    # If we say x.tick(), then python will first check the type of x
    # if x is a Counter object, then it will use the tick method defined in the Counter class
    # if x is a Timer object, then it will use the tick method defined in the Timer class
    # if x is something else, then whatever that is, it better have a tick method, otherwise there is something
    def tick(self):
        # now let's talk about the logic:
        # Seconds should always tick.
        self.seconds.tick()
        # If after ticking the seconds just reset, then we should tick the minutes
        if self.seconds.current_value == self.seconds.maximum_value:
            self.minutes.tick()
            # If after ticking the minutes just reset, then we should tick the hours
            if self.minutes.current_value == self.minutes.maximum_value:
                self.hours.tick()

        # Note that I had a bug in a version of the code that looked as follows:
        # self.seconds.tick()
        # if self.seconds.current_value == self.seconds.maximum_value:
        #     self.minutes.tick()
        # Note that this if statement is not indented
        # if self.minutes.current_value == self.minutes.maximum_value:
        #     self.hours.tick()
        # Can you find the reason why it behaves differently?

test_timer = Timer(1, 30, 0)
boiled_egg_timer = Timer(0, 10, 30)
test_timer.is_over()

# This will use our __str__ method.
print(test_timer)

# While the timer isn't done, print it, then tick
while not test_timer.is_over():
    print(test_timer)
    test_timer.tick()
