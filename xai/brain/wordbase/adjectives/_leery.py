

#calss header
class _LEERY():
	def __init__(self,): 
		self.name = "LEERY"
		self.definitions = [u'not trusting someone or something and usually avoiding him, her, or it if possible: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
