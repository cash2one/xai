

#calss header
class _INSUFFICIENT():
	def __init__(self,): 
		self.name = "INSUFFICIENT"
		self.definitions = [u'not enough: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
