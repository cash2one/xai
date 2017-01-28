

#calss header
class _ORANGE():
	def __init__(self,): 
		self.name = "ORANGE"
		self.definitions = [u'of a colour between red and yellow: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
