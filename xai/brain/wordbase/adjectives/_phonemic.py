

#calss header
class _PHONEMIC():
	def __init__(self,): 
		self.name = "PHONEMIC"
		self.definitions = [u'relating to the phonemes of a language']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
