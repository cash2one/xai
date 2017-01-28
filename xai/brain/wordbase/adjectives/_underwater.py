

#calss header
class _UNDERWATER():
	def __init__(self,): 
		self.name = "UNDERWATER"
		self.definitions = [u'under the surface of the water, especially under the surface of the sea: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
