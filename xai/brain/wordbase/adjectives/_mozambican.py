

#calss header
class _MOZAMBICAN():
	def __init__(self,): 
		self.name = "MOZAMBICAN"
		self.definitions = [u'belonging to or relating to Mozambique or its people']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
