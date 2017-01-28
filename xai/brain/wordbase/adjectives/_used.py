

#calss header
class _USED():
	def __init__(self,): 
		self.name = "USED"
		self.definitions = [u'to be familiar with something or someone: ', u'to become familiar with something or someone: ', u'that has already been put to the purpose it was intended for; not new: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
