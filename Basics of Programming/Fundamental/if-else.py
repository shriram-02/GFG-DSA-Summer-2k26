class Solution:
    def utility(self, number):
        # code here
        if number > 100:
            print("Big")
        elif number < 10:
            print("Small")
        else:
            print("Number")