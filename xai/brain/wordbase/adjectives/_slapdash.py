

#calss header
class _SLAPDASH():
	def __init__(self,): 
		self.name = "SLAPDASH"
		self.definitions = [u'done or made in a hurried and careless way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
