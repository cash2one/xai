

#calss header
class _DISPOSABLE():
	def __init__(self,): 
		self.name = "DISPOSABLE"
		self.definitions = [u'A disposable product is intended to be thrown away after use: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
