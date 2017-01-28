

#calss header
class _WORKABLE():
	def __init__(self,): 
		self.name = "WORKABLE"
		self.definitions = [u'A workable plan or system can be used effectively: ', u'A workable substance can be shaped, changed, or processed in some way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
