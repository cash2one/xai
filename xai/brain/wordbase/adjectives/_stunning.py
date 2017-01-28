

#calss header
class _STUNNING():
	def __init__(self,): 
		self.name = "STUNNING"
		self.definitions = [u'extremely beautiful or attractive: ', u'shocking or very impressive: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
