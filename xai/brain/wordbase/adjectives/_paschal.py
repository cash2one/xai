

#calss header
class _PASCHAL():
	def __init__(self,): 
		self.name = "PASCHAL"
		self.definitions = [u'relating to Easter or to Passover: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
