

#calss header
class _NOTED():
	def __init__(self,): 
		self.name = "NOTED"
		self.definitions = [u'known by many people, especially because of particular qualities: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
