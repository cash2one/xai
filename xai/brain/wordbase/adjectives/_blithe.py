

#calss header
class _BLITHE():
	def __init__(self,): 
		self.name = "BLITHE"
		self.definitions = [u'happy and without worry: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
