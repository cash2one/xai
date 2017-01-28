

#calss header
class _KINDLY():
	def __init__(self,): 
		self.name = "KINDLY"
		self.definitions = [u'in a kind way: ', u'used when asking someone to do something, especially when you are annoyed with them but still want to be polite: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
