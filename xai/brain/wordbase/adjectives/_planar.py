

#calss header
class _PLANAR():
	def __init__(self,): 
		self.name = "PLANAR"
		self.definitions = [u'having a flat or level surface that continues in all directions: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
