

#calss header
class _THROUGH():
	def __init__(self,): 
		self.name = "THROUGH"
		self.definitions = [u'having finished using or doing something: ', u'to achieve success in an exam, competition, etc. and progress to the next stage or a higher level: ', u'A through train or bus goes all the way from one place to another place without the passenger having to change trains or buses.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
