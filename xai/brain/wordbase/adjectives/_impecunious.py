

#calss header
class _IMPECUNIOUS():
	def __init__(self,): 
		self.name = "IMPECUNIOUS"
		self.definitions = [u'having very little money: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
