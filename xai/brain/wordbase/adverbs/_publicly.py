

#calss header
class _PUBLICLY():
	def __init__(self,): 
		self.name = "PUBLICLY"
		self.definitions = [u'If something is done publicly, it is done so that everyone can know about it: ', u'done, owned, or paid for by the government: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
