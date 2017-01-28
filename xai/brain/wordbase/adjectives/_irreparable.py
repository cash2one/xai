

#calss header
class _IRREPARABLE():
	def __init__(self,): 
		self.name = "IRREPARABLE"
		self.definitions = [u'impossible to repair or make right again: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
