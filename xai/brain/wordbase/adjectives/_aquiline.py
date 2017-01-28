

#calss header
class _AQUILINE():
	def __init__(self,): 
		self.name = "AQUILINE"
		self.definitions = [u'of or like an eagle (= large bird): ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
