

#calss header
class _UNUSUAL():
	def __init__(self,): 
		self.name = "UNUSUAL"
		self.definitions = [u'different from others of the same type in a way that is surprising, interesting, or attractive: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
