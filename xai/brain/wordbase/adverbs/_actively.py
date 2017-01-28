

#calss header
class _ACTIVELY():
	def __init__(self,): 
		self.name = "ACTIVELY"
		self.definitions = [u'in a way that involves positive action: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
