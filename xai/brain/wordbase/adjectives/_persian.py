

#calss header
class _PERSIAN():
	def __init__(self,): 
		self.name = "PERSIAN"
		self.definitions = [u'belonging to or relating to Iran, its people, or its language']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
