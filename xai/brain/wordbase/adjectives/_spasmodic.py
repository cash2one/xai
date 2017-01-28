

#calss header
class _SPASMODIC():
	def __init__(self,): 
		self.name = "SPASMODIC"
		self.definitions = [u'happening suddenly for short periods of time and not in a regular way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
