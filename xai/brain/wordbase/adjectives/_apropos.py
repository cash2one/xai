

#calss header
class _APROPOS():
	def __init__(self,): 
		self.name = "APROPOS"
		self.definitions = [u'suitable in a particular situation or at a particular time: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
