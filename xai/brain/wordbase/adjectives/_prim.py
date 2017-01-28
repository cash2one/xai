

#calss header
class _PRIM():
	def __init__(self,): 
		self.name = "PRIM"
		self.definitions = [u'very formal and correct in behaviour and easily shocked by anything rude: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
