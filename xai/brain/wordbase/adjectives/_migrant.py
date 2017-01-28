

#calss header
class _MIGRANT():
	def __init__(self,): 
		self.name = "MIGRANT"
		self.definitions = [u'travelling to a different country or place, often in order to find work: ', u'moving from one place to another at different times of year: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
