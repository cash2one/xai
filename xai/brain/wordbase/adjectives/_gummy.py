

#calss header
class _GUMMY():
	def __init__(self,): 
		self.name = "GUMMY"
		self.definitions = [u'showing the gums: ', u'gummed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
