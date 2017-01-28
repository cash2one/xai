

#calss header
class _WHOLE():
	def __init__(self,): 
		self.name = "WHOLE"
		self.definitions = [u'complete or not divided: ', u'used to emphasize something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
