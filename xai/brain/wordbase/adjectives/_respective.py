

#calss header
class _RESPECTIVE():
	def __init__(self,): 
		self.name = "RESPECTIVE"
		self.definitions = [u'relating or belonging to each of the separate people or things you have just mentioned: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
