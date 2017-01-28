

#calss header
class _TENABLE():
	def __init__(self,): 
		self.name = "TENABLE"
		self.definitions = [u'(of an opinion or position) able to be defended successfully or held for a particular period of time: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
