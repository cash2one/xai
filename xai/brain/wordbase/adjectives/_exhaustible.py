

#calss header
class _EXHAUSTIBLE():
	def __init__(self,): 
		self.name = "EXHAUSTIBLE"
		self.definitions = [u'Exhaustible supplies of something can be used completely so there are none left: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
