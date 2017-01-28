

#calss header
class _BATTERY():
	def __init__(self,): 
		self.name = "BATTERY"
		self.definitions = [u'using a system of producing a large number of eggs cheaply by keeping a lot of chickens in rows of small cages (= boxes made of wire): ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
