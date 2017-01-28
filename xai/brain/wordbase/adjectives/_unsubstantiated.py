

#calss header
class _UNSUBSTANTIATED():
	def __init__(self,): 
		self.name = "UNSUBSTANTIATED"
		self.definitions = [u'not supported by facts: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
