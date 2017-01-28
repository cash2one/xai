

#calss header
class _ACID():
	def __init__(self,): 
		self.name = "ACID"
		self.definitions = [u'containing acid, or having similar qualities to an acid: ', u'used to describe a remark or way of speaking that is cruel or criticizes something in an unkind way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
