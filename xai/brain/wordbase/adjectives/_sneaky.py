

#calss header
class _SNEAKY():
	def __init__(self,): 
		self.name = "SNEAKY"
		self.definitions = [u'doing things in a secret and unfair way: ', u'used to describe something you do, eat, or drink especially when you do it without telling anyone or when you should not really do it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
