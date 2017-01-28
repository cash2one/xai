

#calss header
class _BEAUTEOUS():
	def __init__(self,): 
		self.name = "BEAUTEOUS"
		self.definitions = [u'very attractive to look at']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
