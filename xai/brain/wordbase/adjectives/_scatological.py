

#calss header
class _SCATOLOGICAL():
	def __init__(self,): 
		self.name = "SCATOLOGICAL"
		self.definitions = [u'relating to solid human waste: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
