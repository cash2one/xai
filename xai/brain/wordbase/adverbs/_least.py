

#calss header
class _LEAST():
	def __init__(self,): 
		self.name = "LEAST"
		self.definitions = [u'less than anything or anyone else; the smallest amount or number: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
