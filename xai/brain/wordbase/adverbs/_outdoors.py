

#calss header
class _OUTDOORS():
	def __init__(self,): 
		self.name = "OUTDOORS"
		self.definitions = [u'outside: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
