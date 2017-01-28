

#calss header
class _SPIRITUAL():
	def __init__(self,): 
		self.name = "SPIRITUAL"
		self.definitions = [u'relating to deep feelings and beliefs, especially religious beliefs: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
