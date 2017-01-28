

#calss header
class _DAMAGED():
	def __init__(self,): 
		self.name = "DAMAGED"
		self.definitions = [u'harmed or spoiled: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
