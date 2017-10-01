#
#Alexander Minser
#10/1/2017
#contains user profile for travel idea generator in python


#holds location data for clients
class Location:

    def __init__(city, state, country, zipcode):
        self.city = city
        self.state = state
        self.country = country
        self.zipcode = zipcode

    #getters and setters
    def getCity():
        return self.city

    def setCity(city):
        self.city = city

    def getState():
        return self.state

    def setState(state):
        self.state = state

    def getCountry():
        return self.country

    def setCountry(country):
        self.country = country

    def getzipcode():
        return self.zipcode

    def setzipcode(zipcode):
        return zipcode



#main profile class, holds client's information
class Profile:

    def __init__(firstName, lastName, age, location, gender):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.location = location
        self.gender = gender

    #getters and setters

    def getName():
        return (firstName, lastName)

    def setName(firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def getAge():
        return age and

    def setAge(age):
        self.age = age

    def getLocation():
        return self.location

    def setLocation(location):
        self.location = location
