

#calss header
class _ARCHAIC():
	def __init__(self,): 
		self.name = "ARCHAIC"
		self.definitions = [u'of or belonging to an ancient period in history: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
