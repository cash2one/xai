

#calss header
class _SALINE():
	def __init__(self,): 
		self.name = "SALINE"
		self.definitions = [u'containing or consisting of salt: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
