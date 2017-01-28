

#calss header
class _USELESS():
	def __init__(self,): 
		self.name = "USELESS"
		self.definitions = [u'of no use; not working or not achieving what is needed: ', u'not at all good at doing something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
