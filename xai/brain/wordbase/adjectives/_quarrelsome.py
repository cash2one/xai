

#calss header
class _QUARRELSOME():
	def __init__(self,): 
		self.name = "QUARRELSOME"
		self.definitions = [u'A quarrelsome person repeatedly argues with other people.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
