

#calss header
class _GALORE():
	def __init__(self,): 
		self.name = "GALORE"
		self.definitions = [u'in great amounts or numbers: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
