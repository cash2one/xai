

#calss header
class _OPERABLE():
	def __init__(self,): 
		self.name = "OPERABLE"
		self.definitions = [u'able to be used: ', u'able to be treated by an operation: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
