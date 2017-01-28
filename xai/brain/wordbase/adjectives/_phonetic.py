

#calss header
class _PHONETIC():
	def __init__(self,): 
		self.name = "PHONETIC"
		self.definitions = [u'using special signs to represent the different sounds made by the voice in speech: ', u'A spelling system can be described as phonetic if you can understand how words are pronounced simply by looking at their spelling.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
