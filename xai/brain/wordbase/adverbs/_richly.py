

#calss header
class _RICHLY():
	def __init__(self,): 
		self.name = "RICHLY"
		self.definitions = [u'having a lot of beautiful or expensive decoration, furniture, etc.: ', u'in a very special or valuable way, or in a way that is greater than usual: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
