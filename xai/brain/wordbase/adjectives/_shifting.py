

#calss header
class _SHIFTING():
	def __init__(self,): 
		self.name = "SHIFTING"
		self.definitions = [u'always changing or moving: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
