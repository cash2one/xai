

#calss header
class _INCREMENTAL():
	def __init__(self,): 
		self.name = "INCREMENTAL"
		self.definitions = [u'in a series of amounts: ', u'small: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
