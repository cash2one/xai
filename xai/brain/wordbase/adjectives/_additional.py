

#calss header
class _ADDITIONAL():
	def __init__(self,): 
		self.name = "ADDITIONAL"
		self.definitions = [u'extra: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
