

#calss header
class _CUSTOMARY():
	def __init__(self,): 
		self.name = "CUSTOMARY"
		self.definitions = [u'usual: ', u'traditional: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
