

#calss header
class _UNARMED():
	def __init__(self,): 
		self.name = "UNARMED"
		self.definitions = [u'not armed']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
