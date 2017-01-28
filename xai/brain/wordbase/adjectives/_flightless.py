

#calss header
class _FLIGHTLESS():
	def __init__(self,): 
		self.name = "FLIGHTLESS"
		self.definitions = [u'not able to fly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
