

#calss header
class _INDIAN():
	def __init__(self,): 
		self.name = "INDIAN"
		self.definitions = [u'belonging to or relating to India or its people: ', u'belonging to or relating to Native Americans: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
