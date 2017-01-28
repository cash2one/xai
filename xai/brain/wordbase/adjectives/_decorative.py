

#calss header
class _DECORATIVE():
	def __init__(self,): 
		self.name = "DECORATIVE"
		self.definitions = [u'made to look attractive: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
