

#calss header
class _EPISODIC():
	def __init__(self,): 
		self.name = "EPISODIC"
		self.definitions = [u'happening only sometimes and not regularly: ', u'Episodic stories are divided into several parts, especially when they are broadcast on the television or radio: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
