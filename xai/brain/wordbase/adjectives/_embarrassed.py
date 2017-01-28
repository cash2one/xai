

#calss header
class _EMBARRASSED():
	def __init__(self,): 
		self.name = "EMBARRASSED"
		self.definitions = [u'feeling ashamed or shy: ', u'having no money']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
