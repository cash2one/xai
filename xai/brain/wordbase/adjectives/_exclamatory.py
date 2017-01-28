

#calss header
class _EXCLAMATORY():
	def __init__(self,): 
		self.name = "EXCLAMATORY"
		self.definitions = [u'(of language) expressing surprise, emotion, or pain by means of an exclamation or exclamations: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
