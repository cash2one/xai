

#calss header
class _REASONED():
	def __init__(self,): 
		self.name = "REASONED"
		self.definitions = [u'If an argument is (well) reasoned, it is clear and carefully considered.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
