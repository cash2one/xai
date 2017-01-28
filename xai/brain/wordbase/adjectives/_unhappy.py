

#calss header
class _UNHAPPY():
	def __init__(self,): 
		self.name = "UNHAPPY"
		self.definitions = [u'sad or not satisfied: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
