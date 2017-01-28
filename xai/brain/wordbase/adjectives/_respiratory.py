

#calss header
class _RESPIRATORY():
	def __init__(self,): 
		self.name = "RESPIRATORY"
		self.definitions = [u'relating to breathing: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
