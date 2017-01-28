

#calss header
class _FRETFUL():
	def __init__(self,): 
		self.name = "FRETFUL"
		self.definitions = [u'behaving in a way that shows you are unhappy, worried, or uncomfortable: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
