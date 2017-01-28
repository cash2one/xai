

#calss header
class _BONNY():
	def __init__(self,): 
		self.name = "BONNY"
		self.definitions = [u'beautiful and healthy: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
