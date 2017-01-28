

#calss header
class _HANDY():
	def __init__(self,): 
		self.name = "HANDY"
		self.definitions = [u'useful or convenient: ', u'able to use something skilfully: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
