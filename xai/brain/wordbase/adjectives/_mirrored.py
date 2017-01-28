

#calss header
class _MIRRORED():
	def __init__(self,): 
		self.name = "MIRRORED"
		self.definitions = [u'with a mirror, or pieces of mirror, on it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
