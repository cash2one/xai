

#calss header
class _HUMANLY():
	def __init__(self,): 
		self.name = "HUMANLY"
		self.definitions = [u'able to be done by people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
