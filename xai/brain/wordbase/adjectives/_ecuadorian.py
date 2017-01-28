

#calss header
class _ECUADORIAN():
	def __init__(self,): 
		self.name = "ECUADORIAN"
		self.definitions = [u'belonging to or relating to Ecuador or its people']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
