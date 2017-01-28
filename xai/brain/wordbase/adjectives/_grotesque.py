

#calss header
class _GROTESQUE():
	def __init__(self,): 
		self.name = "GROTESQUE"
		self.definitions = [u'strange and unpleasant, especially in a silly or slightly frightening way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
