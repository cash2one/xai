

#calss header
class _ODDLY():
	def __init__(self,): 
		self.name = "ODDLY"
		self.definitions = [u'in a strange or surprising way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
