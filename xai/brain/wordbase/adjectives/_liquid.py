

#calss header
class _LIQUID():
	def __init__(self,): 
		self.name = "LIQUID"
		self.definitions = [u'in the form of money, rather than investments or property, or able to be changed into money easily: ', u'in the form of a liquid: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
