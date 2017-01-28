

#calss header
class _LINGUISTIC():
	def __init__(self,): 
		self.name = "LINGUISTIC"
		self.definitions = [u'connected with language or the study of language: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
