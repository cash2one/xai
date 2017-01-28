

#calss header
class _UNBROKEN():
	def __init__(self,): 
		self.name = "UNBROKEN"
		self.definitions = [u'continuous and with no pauses: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
