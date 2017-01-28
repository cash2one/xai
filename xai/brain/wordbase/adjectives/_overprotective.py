

#calss header
class _OVERPROTECTIVE():
	def __init__(self,): 
		self.name = "OVERPROTECTIVE"
		self.definitions = [u'wishing to protect someone, especially a child, too much: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
