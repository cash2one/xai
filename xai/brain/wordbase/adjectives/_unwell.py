

#calss header
class _UNWELL():
	def __init__(self,): 
		self.name = "UNWELL"
		self.definitions = [u'not well; ill: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
