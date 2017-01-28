

#calss header
class _PLUMP():
	def __init__(self,): 
		self.name = "PLUMP"
		self.definitions = [u'having a pleasantly soft, rounded body or shape: ', u'polite word for fat: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
