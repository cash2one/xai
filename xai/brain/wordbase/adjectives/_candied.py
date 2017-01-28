

#calss header
class _CANDIED():
	def __init__(self,): 
		self.name = "CANDIED"
		self.definitions = [u'preserved by boiling in sugar: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
