

#calss header
class _ORWELLIAN():
	def __init__(self,): 
		self.name = "ORWELLIAN"
		self.definitions = [u'used to describe a political system in which the government tries to control every part of people\'s lives, similar to that described in the novel "Nineteen Eighty Four", by George Orwell: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
