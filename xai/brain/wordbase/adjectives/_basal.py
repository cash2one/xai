

#calss header
class _BASAL():
	def __init__(self,): 
		self.name = "BASAL"
		self.definitions = [u'forming the bottom layer of something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
