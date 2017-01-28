

#calss header
class _SCRAGGLY():
	def __init__(self,): 
		self.name = "SCRAGGLY"
		self.definitions = [u'growing in a way that is untidy and uneven: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
