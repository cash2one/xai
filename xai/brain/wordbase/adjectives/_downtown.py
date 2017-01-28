

#calss header
class _DOWNTOWN():
	def __init__(self,): 
		self.name = "DOWNTOWN"
		self.definitions = [u'in or to the central part of a city: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
