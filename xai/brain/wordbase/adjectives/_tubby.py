

#calss header
class _TUBBY():
	def __init__(self,): 
		self.name = "TUBBY"
		self.definitions = [u'(of a person) fat: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
