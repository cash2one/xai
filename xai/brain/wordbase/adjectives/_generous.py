

#calss header
class _GENEROUS():
	def __init__(self,): 
		self.name = "GENEROUS"
		self.definitions = [u'willing to give money, help, kindness, etc., especially more than is usual or expected: ', u'larger than usual or expected: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
