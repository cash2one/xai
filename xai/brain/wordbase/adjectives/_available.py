

#calss header
class _AVAILABLE():
	def __init__(self,): 
		self.name = "AVAILABLE"
		self.definitions = [u'able to be bought or used: ', u'If someone is available, they are not busy and therefore able to do something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
