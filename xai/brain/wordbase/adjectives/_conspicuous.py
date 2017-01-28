

#calss header
class _CONSPICUOUS():
	def __init__(self,): 
		self.name = "CONSPICUOUS"
		self.definitions = [u'very noticeable or attracting attention, often in a way that is not wanted: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
