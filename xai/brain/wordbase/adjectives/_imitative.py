

#calss header
class _IMITATIVE():
	def __init__(self,): 
		self.name = "IMITATIVE"
		self.definitions = [u'copying someone or something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
