

#calss header
class _SEPULCHRAL():
	def __init__(self,): 
		self.name = "SEPULCHRAL"
		self.definitions = [u'suggesting death or places where the dead are buried: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
