

#calss header
class _STRIPED():
	def __init__(self,): 
		self.name = "STRIPED"
		self.definitions = [u'Something that is striped has stripes on it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
