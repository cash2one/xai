

#calss header
class _SOUND():
	def __init__(self,): 
		self.name = "SOUND"
		self.definitions = [u'(of sleep) deep and peaceful: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
