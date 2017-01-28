

#calss header
class _LEAN():
	def __init__(self,): 
		self.name = "LEAN"
		self.definitions = [u'Lean meat has little fat.', u'thin and healthy: ', u'If a period of time is lean, there is not enough of something, especially money or food, at that time: ', u'A lean company or organization does not use too many people or spend too much money, so that there is no waste: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
