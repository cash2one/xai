

#calss header
class _SORE():
	def __init__(self,): 
		self.name = "SORE"
		self.definitions = [u'painful and uncomfortable because of injury, infection, or too much use: ', u'angry because you feel you have been unfairly treated: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
