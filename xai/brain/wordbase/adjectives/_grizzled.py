

#calss header
class _GRIZZLED():
	def __init__(self,): 
		self.name = "GRIZZLED"
		self.definitions = [u'having hair that is grey or becoming grey: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
