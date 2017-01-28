

#calss header
class _DILUTE():
	def __init__(self,): 
		self.name = "DILUTE"
		self.definitions = [u'made weaker by diluting: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
