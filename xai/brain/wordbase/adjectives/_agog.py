

#calss header
class _AGOG():
	def __init__(self,): 
		self.name = "AGOG"
		self.definitions = [u'excited and eager to know or see more: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
