

#calss header
class _INTRANSITIVE():
	def __init__(self,): 
		self.name = "INTRANSITIVE"
		self.definitions = [u'(of a verb) having or needing no object: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
