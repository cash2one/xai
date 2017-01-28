

#calss header
class _ARTICULATED():
	def __init__(self,): 
		self.name = "ARTICULATED"
		self.definitions = [u'An articulated vehicle consists of two or more parts that bend where they are joined, in order to help the vehicle turn corners: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
