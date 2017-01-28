

#calss header
class _UNJUSTIFIABLE():
	def __init__(self,): 
		self.name = "UNJUSTIFIABLE"
		self.definitions = [u'unacceptable and wrong because there is no good or fair reason for it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
