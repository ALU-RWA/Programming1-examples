# Before we begin, let's understand the concept of a counter.
# We want to create a tool that counts down numbers. Once reaching 0, the number should reset to
# some max value, before decreasing again. This is the same behaviour as what you see in a timer, but
# can apply in other contexts too.

# The objects we create should therefore hold a number that decreases, but should also know what to reset it to
class Counter:

    # We start as usual by our constructor.
    def __init__(self, current_value, maximum_value):
        # This print is only here to show us the constructor is being used, you may delete it.
        print("We are using the constructor")

        #if the current_value is bigger than the max
        # set the object's current value to the max
        self.maximum_value = maximum_value

        if current_value > maximum_value:
            self.current_value = maximum_value
        else:
            self.current_value = current_value

    # should return a String that represents the object
    # This will be automatically called whenever Python needs
    # to turn your object into a String
    def __str__(self):
        return str(self.current_value)

    # If the current_value is more than 0, simply decrease it.
    # Otherwise, reset
    def tick(self):
        if self.current_value > 0:
            self.current_value = self.current_value - 1
        else:
            self.reset() # Note that you can call methods within other methods.

    # reset the current value to maximum value.
    def reset(self):
        self.current_value = self.maximum_value


# test1 = Counter(9, 49)
# test1.tick()
# test1.tick()
# print(test1.current_value)
# test1.reset()
# print(test1.current_value)
#
# test2 = Counter(15, 49)
# test3 = Counter(19, 88)
# test4 = Counter(90, 490)
#
# x = str(test2)
# print(x)
# print(test1)
# print(test2)
# print(test3)
# print(test4)

#
# while True:
#     print(test1.current_value)
#     test1.tick()
#
# # test2 = Counter(30, 59)
# # print(test2.current_value)
# # test2.tick()
# # print(test2.current_value)
# #
# # test3 = Counter(100, 59)
# # print(test3.current_value)
