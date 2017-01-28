

#calss header
class _SLAVISHLY():
	def __init__(self,): 
		self.name = "SLAVISHLY"
		self.definitions = [u'obeying completely; without any ideas of your own: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
