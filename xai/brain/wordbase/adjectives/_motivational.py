

#calss header
class _MOTIVATIONAL():
	def __init__(self,): 
		self.name = "MOTIVATIONAL"
		self.definitions = [u'giving you motivation (= enthusiasm): ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
