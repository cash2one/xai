

#calss header
class _HEADY():
	def __init__(self,): 
		self.name = "HEADY"
		self.definitions = [u'having a powerful effect, making you feel slightly drunk or excited: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
