

#calss header
class _GAUCHE():
	def __init__(self,): 
		self.name = "GAUCHE"
		self.definitions = [u'awkward and uncomfortable with other people, especially because young and without experience: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
