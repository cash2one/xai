

#calss header
class _CUTE():
	def __init__(self,): 
		self.name = "CUTE"
		self.definitions = [u'(especially of something or someone small or young) pleasant and attractive: ', u'trying to be clever, sometimes in a rude or unpleasant way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
