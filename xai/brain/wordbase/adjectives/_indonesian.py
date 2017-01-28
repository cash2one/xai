

#calss header
class _INDONESIAN():
	def __init__(self,): 
		self.name = "INDONESIAN"
		self.definitions = [u'belonging to or relating to Indonesia, its people, or its language']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
