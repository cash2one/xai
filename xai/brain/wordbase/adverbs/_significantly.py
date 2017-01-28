

#calss header
class _SIGNIFICANTLY():
	def __init__(self,): 
		self.name = "SIGNIFICANTLY"
		self.definitions = [u'in a way that is easy to see or by a large amount: ', u'in a way that suggests a special meaning: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
