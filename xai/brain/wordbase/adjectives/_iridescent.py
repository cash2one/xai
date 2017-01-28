

#calss header
class _IRIDESCENT():
	def __init__(self,): 
		self.name = "IRIDESCENT"
		self.definitions = [u'showing many bright colours that change with movement: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
