

#calss header
class _UNSAFE():
	def __init__(self,): 
		self.name = "UNSAFE"
		self.definitions = [u'not safe', u'An unsafe conviction (= legal decision that someone is guilty) may be wrong because it is based on bad evidence: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
