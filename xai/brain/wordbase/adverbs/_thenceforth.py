

#calss header
class _THENCEFORTH():
	def __init__(self,): 
		self.name = "THENCEFORTH"
		self.definitions = [u'after that; from that time forward: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
