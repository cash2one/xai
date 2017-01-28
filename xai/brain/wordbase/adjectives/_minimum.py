

#calss header
class _MINIMUM():
	def __init__(self,): 
		self.name = "MINIMUM"
		self.definitions = [u'used to describe something that is the smallest or least allowed or possible: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
