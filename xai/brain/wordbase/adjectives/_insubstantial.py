

#calss header
class _INSUBSTANTIAL():
	def __init__(self,): 
		self.name = "INSUBSTANTIAL"
		self.definitions = [u'not enough or not strong enough: ', u'not existing as a physical person or thing: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
