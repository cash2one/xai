

#calss header
class _LEGAL():
	def __init__(self,): 
		self.name = "LEGAL"
		self.definitions = [u'connected with the law: ', u'allowed by the law: ', u'used to refer to a standard size of paper in the US, 8.5 inches by 14 inches: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
