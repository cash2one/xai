

#calss header
class _ATAVISTIC():
	def __init__(self,): 
		self.name = "ATAVISTIC"
		self.definitions = [u'happening because of a very old habit from a long time ago in human history, not because of a conscious decision or because it is necessary now: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
