

#calss header
class _GLITTERY():
	def __init__(self,): 
		self.name = "GLITTERY"
		self.definitions = [u'producing a lot of small flashes of reflected light: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
