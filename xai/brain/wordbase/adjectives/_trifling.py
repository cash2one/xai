

#calss header
class _TRIFLING():
	def __init__(self,): 
		self.name = "TRIFLING"
		self.definitions = [u'A trifling matter or amount of money is small or not important: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
