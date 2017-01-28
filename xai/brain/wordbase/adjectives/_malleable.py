

#calss header
class _MALLEABLE():
	def __init__(self,): 
		self.name = "MALLEABLE"
		self.definitions = [u'A malleable substance is easily changed into a new shape: ', u'easily influenced, trained, or controlled: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
