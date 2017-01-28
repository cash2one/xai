

#calss header
class _IMPOSING():
	def __init__(self,): 
		self.name = "IMPOSING"
		self.definitions = [u'having an appearance that looks important or causes admiration: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
