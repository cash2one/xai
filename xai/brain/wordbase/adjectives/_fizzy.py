

#calss header
class _FIZZY():
	def __init__(self,): 
		self.name = "FIZZY"
		self.definitions = [u'having a lot of bubbles: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
