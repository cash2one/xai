

#calss header
class _POTTY():
	def __init__(self,): 
		self.name = "POTTY"
		self.definitions = [u'silly or slightly crazy: ', u'to like something very much: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
