

#calss header
class _INCONSIDERATE():
	def __init__(self,): 
		self.name = "INCONSIDERATE"
		self.definitions = [u'not thinking or worrying about other people or their feelings: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
