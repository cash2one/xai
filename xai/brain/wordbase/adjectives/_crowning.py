

#calss header
class _CROWNING():
	def __init__(self,): 
		self.name = "CROWNING"
		self.definitions = [u'A crowning event or achievement is the best or most important one: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
