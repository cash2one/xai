

#calss header
class _RUEFUL():
	def __init__(self,): 
		self.name = "RUEFUL"
		self.definitions = [u'feeling sorry and wishing that something had not happened: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
