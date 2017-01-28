

#calss header
class _GOSSAMER():
	def __init__(self,): 
		self.name = "GOSSAMER"
		self.definitions = [u'very delicate and light: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
