

#calss header
class _TRANSCENDENT():
	def __init__(self,): 
		self.name = "TRANSCENDENT"
		self.definitions = [u'greater, better, more important, or going past or above all others: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
