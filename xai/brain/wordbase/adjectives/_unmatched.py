

#calss header
class _UNMATCHED():
	def __init__(self,): 
		self.name = "UNMATCHED"
		self.definitions = [u'having no equal; better than any other of the same type: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
