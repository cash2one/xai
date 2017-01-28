

#calss header
class _OFFENSIVE():
	def __init__(self,): 
		self.name = "OFFENSIVE"
		self.definitions = [u'causing offence: ', u'unpleasant: ', u'used for attacking: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
