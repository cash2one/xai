

#calss header
class _CARSICK():
	def __init__(self,): 
		self.name = "CARSICK"
		self.definitions = [u'feeling that you want to vomit because of the movement of a car']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
