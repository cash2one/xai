

#calss header
class _LUMINOUS():
	def __init__(self,): 
		self.name = "LUMINOUS"
		self.definitions = [u'producing or reflecting bright light (especially in the dark): ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
