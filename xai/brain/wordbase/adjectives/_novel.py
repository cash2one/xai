

#calss header
class _NOVEL():
	def __init__(self,): 
		self.name = "NOVEL"
		self.definitions = [u'new and original, not like anything seen before: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
