

#calss header
class _DOGGED():
	def __init__(self,): 
		self.name = "DOGGED"
		self.definitions = [u'very determined to do something, even if it is very difficult: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
