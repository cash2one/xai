

#calss header
class _FLOURY():
	def __init__(self,): 
		self.name = "FLOURY"
		self.definitions = [u'covered in flour, or tasting or feeling like flour: ', u'Floury potatoes are dry and break into small pieces when they are cooked.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
