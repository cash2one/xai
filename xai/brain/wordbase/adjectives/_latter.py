

#calss header
class _LATTER():
	def __init__(self,): 
		self.name = "LATTER"
		self.definitions = [u'near or towards the end of something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
