

#calss header
class _STEADILY():
	def __init__(self,): 
		self.name = "STEADILY"
		self.definitions = [u'gradually: ', u'calmly and in a controlled way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
