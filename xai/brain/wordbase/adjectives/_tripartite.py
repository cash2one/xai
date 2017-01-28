

#calss header
class _TRIPARTITE():
	def __init__(self,): 
		self.name = "TRIPARTITE"
		self.definitions = [u'involving three people or organizations, or existing in three parts: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
