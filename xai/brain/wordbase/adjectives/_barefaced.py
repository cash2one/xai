

#calss header
class _BAREFACED():
	def __init__(self,): 
		self.name = "BAREFACED"
		self.definitions = [u'not trying to hide your bad behaviour: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
