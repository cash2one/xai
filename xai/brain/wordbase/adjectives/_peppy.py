

#calss header
class _PEPPY():
	def __init__(self,): 
		self.name = "PEPPY"
		self.definitions = [u'having a lot of energy or activity: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
