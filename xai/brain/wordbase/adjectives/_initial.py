

#calss header
class _INITIAL():
	def __init__(self,): 
		self.name = "INITIAL"
		self.definitions = [u'of or at the beginning: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
