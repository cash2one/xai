

#calss header
class _BESIDES():
	def __init__(self,): 
		self.name = "BESIDES"
		self.definitions = [u'in addition to; also: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
