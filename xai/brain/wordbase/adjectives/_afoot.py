

#calss header
class _AFOOT():
	def __init__(self,): 
		self.name = "AFOOT"
		self.definitions = [u'happening or being planned or prepared: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
