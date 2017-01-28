

#calss header
class _ARTIFICIAL():
	def __init__(self,): 
		self.name = "ARTIFICIAL"
		self.definitions = [u'made by people, often as a copy of something natural: ', u'not sincere: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
