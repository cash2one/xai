

#calss header
class _INCONTROVERTIBLE():
	def __init__(self,): 
		self.name = "INCONTROVERTIBLE"
		self.definitions = [u'impossible to doubt because of being obviously true: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
