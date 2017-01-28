

#calss header
class _CALCULATED():
	def __init__(self,): 
		self.name = "CALCULATED"
		self.definitions = [u'planned or arranged in order to produce a particular effect: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
