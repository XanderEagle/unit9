class Dog:

    def __init__(self, name):
        self.name = name
        self.trick_list = []

    def dog_name(self):
        return self.name

    def print_name(self):
        print(self.name)

    def sit(self):
        print(self.name + " sits")
        self.trick_list.append("sit")

    def roll_over(self):
        print(self.name + " rolls over")
        self.trick_list.append("roll over")

    def shake(self):
        print(self.name + " shakes")
        self.trick_list.append("shake")

    def print_trick_list(self):
        if len(self.trick_list) == 0:
            print(self.name + " didn't hear you say the trick.")
        else:
            print(self.name + " doesn't know this trick.")
            for x in self.trick_list:
                print(x)
