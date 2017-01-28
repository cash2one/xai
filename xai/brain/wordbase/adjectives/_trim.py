

#calss header
class _TRIM():
	def __init__(self,): 
		self.name = "TRIM"
		self.definitions = [u'thin in an attractive and healthy way: ', u'tidy and well ordered: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
