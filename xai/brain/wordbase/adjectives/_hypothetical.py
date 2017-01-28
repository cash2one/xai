

#calss header
class _HYPOTHETICAL():
	def __init__(self,): 
		self.name = "HYPOTHETICAL"
		self.definitions = [u'imagined or suggested but not necessarily real or true: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
