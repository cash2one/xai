

#calss header
class _FOREARMED():
	def __init__(self,): 
		self.name = "FOREARMED"
		self.definitions = [u'\u2192\xa0 forewarned is forearmed ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
