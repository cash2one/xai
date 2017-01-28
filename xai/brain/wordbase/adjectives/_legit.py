

#calss header
class _LEGIT():
	def __init__(self,): 
		self.name = "LEGIT"
		self.definitions = [u'\u2192\xa0 legitimate adjective : ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
