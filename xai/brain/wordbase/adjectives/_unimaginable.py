

#calss header
class _UNIMAGINABLE():
	def __init__(self,): 
		self.name = "UNIMAGINABLE"
		self.definitions = [u'Something that is unimaginable is difficult to imagine because it is so bad, good, big, etc.: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
