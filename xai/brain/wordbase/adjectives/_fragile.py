

#calss header
class _FRAGILE():
	def __init__(self,): 
		self.name = "FRAGILE"
		self.definitions = [u'easily damaged, broken, or harmed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
