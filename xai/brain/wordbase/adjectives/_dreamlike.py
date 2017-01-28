

#calss header
class _DREAMLIKE():
	def __init__(self,): 
		self.name = "DREAMLIKE"
		self.definitions = [u'as if in a dream and therefore not real: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
