

#calss header
class _PRESSED():
	def __init__(self,): 
		self.name = "PRESSED"
		self.definitions = [u'to be in a difficult situation because you do not have enough time, money, space, etc.: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
