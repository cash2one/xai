

#calss header
class _MATRONLY():
	def __init__(self,): 
		self.name = "MATRONLY"
		self.definitions = [u'A matronly woman, usually one who is not young, is fat and does not dress in a fashionable way.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
