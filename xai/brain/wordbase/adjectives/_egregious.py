

#calss header
class _EGREGIOUS():
	def __init__(self,): 
		self.name = "EGREGIOUS"
		self.definitions = [u'extremely bad in a way that is very noticeable: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
