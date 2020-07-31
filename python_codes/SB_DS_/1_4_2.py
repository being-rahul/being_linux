class Dog:
	def __init__(self, name, month, date, year, speakText):
		self.name=name
		self.month=month
		self.date=date
		self.year=year
		self.speakText=speakText

	def speak(self):
		return self.speakText

	def getName(self):
		return self.name

	def dob(self):
		return str(self.month) + "/" + str(self.date) + "/" + str(self.year)

	def changeBark(self,bark):
		self.speakText=bark

	def __add__(self,otherDog):
		return Dog("Puppy of " + self.name + " and " + otherDog.name,
		 self.month, self.date, self.year + 1, self.speakText + otherDog.speakText)

maleDog=Dog("jackie",5,20,2000,"woof")

print(maleDog.speak())
print(maleDog.getName())
print(maleDog.dob())
maleDog.changeBark("bhao bhao")
print(maleDog.speak())	

femaleDog=Dog("sofi",1,22,2001,"woo")

print(femaleDog.speak())
print(femaleDog.getName())
print(femaleDog.dob())

puppy= maleDog + femaleDog
print(puppy.speak())
print(puppy.getName())
print(puppy.dob())