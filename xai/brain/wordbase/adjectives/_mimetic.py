

#calss header
class _MIMETIC():
	def __init__(self,): 
		self.name = "MIMETIC"
		self.definitions = [u'copying or appearing the same as something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
