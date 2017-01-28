

#calss header
class _CONGRUOUS():
	def __init__(self,): 
		self.name = "CONGRUOUS"
		self.definitions = [u'the same as, or in agreement with, other facts or principles: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
