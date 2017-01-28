

#calss header
class _COCKEYED():
	def __init__(self,): 
		self.name = "COCKEYED"
		self.definitions = [u'not straight, but sloping to one side: ', u'used to describe a plan or idea that is stupid, not suitable, or not likely to be successful: ', u'having drunk too much alcohol']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
