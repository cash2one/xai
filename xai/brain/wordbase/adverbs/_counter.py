

#calss header
class _COUNTER():
	def __init__(self,): 
		self.name = "COUNTER"
		self.definitions = [u'in a way that opposes something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
