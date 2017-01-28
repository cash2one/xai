

#calss header
class _UNDONE():
	def __init__(self,): 
		self.name = "UNDONE"
		self.definitions = [u'unfastened: ', u'to be without hope for the future, having experienced great disappointment, loss of money, etc.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
