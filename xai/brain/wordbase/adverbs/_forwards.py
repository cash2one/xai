

#calss header
class _FORWARDS():
	def __init__(self,): 
		self.name = "FORWARDS"
		self.definitions = [u'\u2192\xa0 forward ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
