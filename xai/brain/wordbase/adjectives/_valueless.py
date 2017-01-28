

#calss header
class _VALUELESS():
	def __init__(self,): 
		self.name = "VALUELESS"
		self.definitions = [u'not worth any money: ', u'not important or helpful: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
