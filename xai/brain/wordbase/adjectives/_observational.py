

#calss header
class _OBSERVATIONAL():
	def __init__(self,): 
		self.name = "OBSERVATIONAL"
		self.definitions = [u'involving watching someone or something carefully and closely, in order to learn something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
