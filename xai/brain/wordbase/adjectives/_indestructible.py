

#calss header
class _INDESTRUCTIBLE():
	def __init__(self,): 
		self.name = "INDESTRUCTIBLE"
		self.definitions = [u'impossible to destroy or break: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
