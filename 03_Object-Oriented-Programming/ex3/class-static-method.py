class Date():

    def __init__(self, day=0, month=0, year=0):
        print('Constructor ' + str(day))
        self.day = day
        self.month = month
        self.year = year

    @staticmethod
    def getStaticInstance():
        return Date(1)

    @classmethod
    def getClassInstance(cls):
        return cls(2)

    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        date1 = cls(day, month, year)
        return date1

    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999


date1 = Date.getStaticInstance()
date2 = Date.getClassInstance()

date3 = Date.from_string('11-09-2012')

is_date = Date.is_date_valid('11-09-2012')

print(date1)
print(date2)
print(date3)
print(is_date)

# Constructor 1
# Constructor 2
# Constructor 11
# <__main__.Date object at 0x107baf4e0>
# <__main__.Date object at 0x107baf518>
# <__main__.Date object at 0x107baf630>
# True