

#calss header
class _TOMORROW():
	def __init__(self,): 
		self.name = "TOMORROW"
		self.definitions = [u'(on) the day after today: ', u'used more generally to mean the future: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
