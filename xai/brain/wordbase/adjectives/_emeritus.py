

#calss header
class _EMERITUS():
	def __init__(self,): 
		self.name = "EMERITUS"
		self.definitions = [u'no longer having a position, especially in a college or university, but keeping the title of the position: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
