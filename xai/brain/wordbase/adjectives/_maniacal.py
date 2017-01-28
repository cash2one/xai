

#calss header
class _MANIACAL():
	def __init__(self,): 
		self.name = "MANIACAL"
		self.definitions = [u'A maniacal cry or laugh is loud and wild: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
