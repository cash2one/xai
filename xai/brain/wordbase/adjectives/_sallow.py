

#calss header
class _SALLOW():
	def __init__(self,): 
		self.name = "SALLOW"
		self.definitions = [u'(of white-skinned people) yellowish and looking unhealthy: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
