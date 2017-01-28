

#calss header
class _SNEAKING():
	def __init__(self,): 
		self.name = "SNEAKING"
		self.definitions = [u'If you have a sneaking feeling about someone or something, you have that feeling, although you are not certain it is correct: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
