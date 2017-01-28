

#calss header
class _MANLY():
	def __init__(self,): 
		self.name = "MANLY"
		self.definitions = [u'having the qualities that people think a man should have: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
