

#calss header
class _LUSTY():
	def __init__(self,): 
		self.name = "LUSTY"
		self.definitions = [u'healthy, energetic, and full of strength and power: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
