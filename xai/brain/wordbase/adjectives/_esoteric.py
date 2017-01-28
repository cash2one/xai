

#calss header
class _ESOTERIC():
	def __init__(self,): 
		self.name = "ESOTERIC"
		self.definitions = [u'very unusual and understood or liked by only a small number of people, especially those with special knowledge: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
