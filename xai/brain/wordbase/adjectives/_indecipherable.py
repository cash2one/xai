

#calss header
class _INDECIPHERABLE():
	def __init__(self,): 
		self.name = "INDECIPHERABLE"
		self.definitions = [u'unable to be read or understood: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
