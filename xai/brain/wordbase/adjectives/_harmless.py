

#calss header
class _HARMLESS():
	def __init__(self,): 
		self.name = "HARMLESS"
		self.definitions = [u'not able or not likely to cause harm: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
