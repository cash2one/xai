

#calss header
class _PLEBEIAN():
	def __init__(self,): 
		self.name = "PLEBEIAN"
		self.definitions = [u'belonging to a low social class: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
