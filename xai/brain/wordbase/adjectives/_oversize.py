

#calss header
class _OVERSIZE():
	def __init__(self,): 
		self.name = "OVERSIZE"
		self.definitions = [u'bigger than usual, or too big: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
