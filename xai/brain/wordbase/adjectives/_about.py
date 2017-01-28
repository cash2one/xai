

#calss header
class _ABOUT():
	def __init__(self,): 
		self.name = "ABOUT"
		self.definitions = [u'to be going to do something very soon: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
