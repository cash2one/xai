

#calss header
class _MORTIFYING():
	def __init__(self,): 
		self.name = "MORTIFYING"
		self.definitions = [u'very embarrassing: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
