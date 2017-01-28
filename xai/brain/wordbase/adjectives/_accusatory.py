

#calss header
class _ACCUSATORY():
	def __init__(self,): 
		self.name = "ACCUSATORY"
		self.definitions = [u'suggesting that you think someone has done something bad: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
