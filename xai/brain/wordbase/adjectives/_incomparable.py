

#calss header
class _INCOMPARABLE():
	def __init__(self,): 
		self.name = "INCOMPARABLE"
		self.definitions = [u'so good or great that nothing or no one else could achieve the same standard: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
