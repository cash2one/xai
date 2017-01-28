

#calss header
class _APPRECIATIVE():
	def __init__(self,): 
		self.name = "APPRECIATIVE"
		self.definitions = [u'showing that you understand how good something is, or are grateful for something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
