

#calss header
class _GRADUALLY():
	def __init__(self,): 
		self.name = "GRADUALLY"
		self.definitions = [u'slowly over a period of time or a distance: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
