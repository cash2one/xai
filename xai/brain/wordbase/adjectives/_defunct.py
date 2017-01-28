

#calss header
class _DEFUNCT():
	def __init__(self,): 
		self.name = "DEFUNCT"
		self.definitions = [u'no longer existing, living, or working correctly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
