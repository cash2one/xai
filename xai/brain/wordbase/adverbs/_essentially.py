

#calss header
class _ESSENTIALLY():
	def __init__(self,): 
		self.name = "ESSENTIALLY"
		self.definitions = [u'relating to the most important characteristics or ideas of something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
