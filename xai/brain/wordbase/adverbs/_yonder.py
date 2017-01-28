

#calss header
class _YONDER():
	def __init__(self,): 
		self.name = "YONDER"
		self.definitions = [u'in the place or direction shown; over there']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
