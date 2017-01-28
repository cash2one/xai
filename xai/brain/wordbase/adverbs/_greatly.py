

#calss header
class _GREATLY():
	def __init__(self,): 
		self.name = "GREATLY"
		self.definitions = [u'very much, used especially to show how much you feel or experience something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
