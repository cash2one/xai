

#calss header
class _MEDIAN():
	def __init__(self,): 
		self.name = "MEDIAN"
		self.definitions = [u'The median value is the middle one in a set of values arranged in order of size: ', u'near the centre of the body, rather than the sides: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
