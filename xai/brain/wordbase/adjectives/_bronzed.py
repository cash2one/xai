

#calss header
class _BRONZED():
	def __init__(self,): 
		self.name = "BRONZED"
		self.definitions = [u'If someone is bronzed, their skin is attractively brown because they have been in the sun: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
