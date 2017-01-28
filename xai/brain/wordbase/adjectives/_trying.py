

#calss header
class _TRYING():
	def __init__(self,): 
		self.name = "TRYING"
		self.definitions = [u'annoying and difficult: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
