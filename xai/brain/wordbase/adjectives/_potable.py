

#calss header
class _POTABLE():
	def __init__(self,): 
		self.name = "POTABLE"
		self.definitions = [u'clean and safe to drink: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
