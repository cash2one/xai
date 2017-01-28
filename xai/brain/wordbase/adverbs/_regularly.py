

#calss header
class _REGULARLY():
	def __init__(self,): 
		self.name = "REGULARLY"
		self.definitions = [u'often: ', u'with equal or similar amounts of space or time between one and the next: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
