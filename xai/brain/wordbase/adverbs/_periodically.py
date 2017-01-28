

#calss header
class _PERIODICALLY():
	def __init__(self,): 
		self.name = "PERIODICALLY"
		self.definitions = [u'in a way that is repeated after a particular period of time: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
