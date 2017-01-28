

#calss header
class _MEANDERING():
	def __init__(self,): 
		self.name = "MEANDERING"
		self.definitions = [u'moving slowly in no particular direction or with no clear purpose: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
