

#calss header
class _ARTHRITIC():
	def __init__(self,): 
		self.name = "ARTHRITIC"
		self.definitions = [u'suffering from or affected by arthritis: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
