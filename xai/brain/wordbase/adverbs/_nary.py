

#calss header
class _NARY():
	def __init__(self,): 
		self.name = "NARY"
		self.definitions = [u'not one or none at all; used for emphasis: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
