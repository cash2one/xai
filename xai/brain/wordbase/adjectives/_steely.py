

#calss header
class _STEELY():
	def __init__(self,): 
		self.name = "STEELY"
		self.definitions = [u'like steel in colour: ', u'very strong and determined: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
