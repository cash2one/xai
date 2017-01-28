

#calss header
class _PERTINACIOUS():
	def __init__(self,): 
		self.name = "PERTINACIOUS"
		self.definitions = [u'very determined and refusing to be defeated by problems: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
