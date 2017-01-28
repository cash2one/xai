

#calss header
class _CONGENITAL():
	def __init__(self,): 
		self.name = "CONGENITAL"
		self.definitions = [u'A congenital disease or condition exists at or from birth: ', u'used to say that someone always shows a particular bad quality: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
