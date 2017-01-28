

#calss header
class _NEUROTIC():
	def __init__(self,): 
		self.name = "NEUROTIC"
		self.definitions = [u'behaving strangely or in an anxious (= worried and nervous) way, often because you have a mental illness: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
