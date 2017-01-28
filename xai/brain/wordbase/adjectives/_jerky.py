

#calss header
class _JERKY():
	def __init__(self,): 
		self.name = "JERKY"
		self.definitions = [u'quick and sudden: ', u'not smooth and pleasant: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
