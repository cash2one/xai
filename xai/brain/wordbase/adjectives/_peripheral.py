

#calss header
class _PERIPHERAL():
	def __init__(self,): 
		self.name = "PERIPHERAL"
		self.definitions = [u'Something that is peripheral is not as important as something else: ', u'happening at the edge of something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
