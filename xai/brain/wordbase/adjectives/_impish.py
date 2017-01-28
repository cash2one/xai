

#calss header
class _IMPISH():
	def __init__(self,): 
		self.name = "IMPISH"
		self.definitions = [u"showing a child's pleasure in enjoying yourself and making trouble: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
