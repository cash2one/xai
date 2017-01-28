

#calss header
class _STRAY():
	def __init__(self,): 
		self.name = "STRAY"
		self.definitions = [u'Stray things have moved apart from similar things and are not in their expected or intended place: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
