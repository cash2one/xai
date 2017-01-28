

#calss header
class _ADJACENT():
	def __init__(self,): 
		self.name = "ADJACENT"
		self.definitions = [u'very near, next to, or touching: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
