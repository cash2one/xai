

#calss header
class _SUPPOSEDLY():
	def __init__(self,): 
		self.name = "SUPPOSEDLY"
		self.definitions = [u'used to show that you do not believe that something you have been told is true: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
