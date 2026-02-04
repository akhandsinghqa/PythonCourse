class Names:

    @property
    def name(self):
        print("Getting name.......")
        return f"{self._fname}{self._mname}{self._lname}"

    @name.setter
    def name(self, value):
        print("Setting the name.....")
        splitname = value.split(" ")
        if len(splitname) == 2:
            self._fname = splitname[0] + " "
            self._mname = ""
            self._lname = splitname[1]
        elif len(splitname) == 3:
            self._fname = splitname[0] + " "
            self._mname = splitname[1] + " "
            self._lname = splitname[2]


nobject = Names()
nobject.name = input("Enter the name:")
print(nobject.name)
