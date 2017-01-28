

#calss header
class _STRANGLED():
	def __init__(self,): 
		self.name = "STRANGLED"
		self.definitions = [u'A strangled sound is a weak, high, interrupted sound made by an extremely frightened or worried and nervous person: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
