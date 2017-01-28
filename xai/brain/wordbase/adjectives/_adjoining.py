

#calss header
class _ADJOINING():
	def __init__(self,): 
		self.name = "ADJOINING"
		self.definitions = [u'near, next to, or touching: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
