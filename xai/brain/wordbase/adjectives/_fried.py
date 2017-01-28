

#calss header
class _FRIED():
	def __init__(self,): 
		self.name = "FRIED"
		self.definitions = [u'cooked in hot oil or fat: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
