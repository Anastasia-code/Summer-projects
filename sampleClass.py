class Dob:
    def __init__(self, month, date, year):
        self.month=int(month)
        self.date=int(date)
        self.year=int(year)

    def zodiac(self):
        if self.month==1 and self.date<=19:
            zodiac="capricorn"
        #write other zodiac cut offs
        print(zodiac)

person1=Dob(1,1,2000)
person1.zodiac()
