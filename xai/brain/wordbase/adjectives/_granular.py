

#calss header
class _GRANULAR():
	def __init__(self,): 
		self.name = "GRANULAR"
		self.definitions = [u'made of, or seeming like, granules: ', u'including small details: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
