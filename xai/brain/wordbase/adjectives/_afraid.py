

#calss header
class _AFRAID():
	def __init__(self,): 
		self.name = "AFRAID"
		self.definitions = [u'feeling fear, or feeling worry about the possible results of a particular situation: ', u'used to politely introduce bad news or disagreement: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
