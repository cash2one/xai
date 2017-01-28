

#calss header
class _TAMIL():
	def __init__(self,): 
		self.name = "TAMIL"
		self.definitions = [u'belonging to a group of people who form part of the population of Sri Lanka and also live in India and Southeast Asia']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
