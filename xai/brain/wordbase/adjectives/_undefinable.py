

#calss header
class _UNDEFINABLE():
	def __init__(self,): 
		self.name = "UNDEFINABLE"
		self.definitions = [u'\u2192\xa0 indefinable ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
