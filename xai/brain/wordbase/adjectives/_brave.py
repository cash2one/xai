

#calss header
class _BRAVE():
	def __init__(self,): 
		self.name = "BRAVE"
		self.definitions = [u'showing no fear of dangerous or difficult things: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
