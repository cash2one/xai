

#calss header
class _CHARITABLY():
	def __init__(self,): 
		self.name = "CHARITABLY"
		self.definitions = [u'in a kind way, not judging other people in a severe way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
