

#calss header
class _FORMULAIC():
	def __init__(self,): 
		self.name = "FORMULAIC"
		self.definitions = [u'containing or consisting of fixed and repeated groups of words or ideas: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
