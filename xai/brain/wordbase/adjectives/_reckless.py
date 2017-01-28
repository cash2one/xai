

#calss header
class _RECKLESS():
	def __init__(self,): 
		self.name = "RECKLESS"
		self.definitions = [u'doing something dangerous and not worrying about the risks and the possible results: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
