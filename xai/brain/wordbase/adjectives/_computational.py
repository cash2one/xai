

#calss header
class _COMPUTATIONAL():
	def __init__(self,): 
		self.name = "COMPUTATIONAL"
		self.definitions = [u'involving the calculation of answers, amounts, results, etc.: ', u'using computers to study something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
