

#calss header
class _KAPUT():
	def __init__(self,): 
		self.name = "KAPUT"
		self.definitions = [u'not working correctly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
