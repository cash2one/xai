

#calss header
class _UNFORGETTABLE():
	def __init__(self,): 
		self.name = "UNFORGETTABLE"
		self.definitions = [u'An unforgettable experience has such a strong effect or influence on you that you cannot forget it.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
