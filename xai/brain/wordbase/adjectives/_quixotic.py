

#calss header
class _QUIXOTIC():
	def __init__(self,): 
		self.name = "QUIXOTIC"
		self.definitions = [u'having or showing ideas that are different and unusual but not practical or likely to succeed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
