

#calss header
class _COURTEOUS():
	def __init__(self,): 
		self.name = "COURTEOUS"
		self.definitions = [u'polite and showing respect: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
