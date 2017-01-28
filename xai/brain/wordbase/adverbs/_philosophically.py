

#calss header
class _PHILOSOPHICALLY():
	def __init__(self,): 
		self.name = "PHILOSOPHICALLY"
		self.definitions = [u'in a way that calmly accepts a difficult situation']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
