

#calss header
class _BENGALI():
	def __init__(self,): 
		self.name = "BENGALI"
		self.definitions = [u'belonging to or relating to Bangladesh and West Bengal or their people']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
