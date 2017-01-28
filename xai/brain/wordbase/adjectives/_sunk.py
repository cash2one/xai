

#calss header
class _SUNK():
	def __init__(self,): 
		self.name = "SUNK"
		self.definitions = [u'experiencing serious trouble, or unable to solve a problem: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
