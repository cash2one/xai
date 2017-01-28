

#calss header
class _BALD():
	def __init__(self,): 
		self.name = "BALD"
		self.definitions = [u'with little or no hair on the head: ', u'completely bald: ', u'basic and with no unnecessary words or detail: ', u'a bald tyre is one that has worn away to become very smooth and is therefore dangerous: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
