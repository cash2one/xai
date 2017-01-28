

#calss header
class _UNENFORCEABLE():
	def __init__(self,): 
		self.name = "UNENFORCEABLE"
		self.definitions = [u'If a rule or law is unenforceable, it is impossible to force people to obey it.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
