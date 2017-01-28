

#calss header
class _DAILY():
	def __init__(self,): 
		self.name = "DAILY"
		self.definitions = [u'happening on or relating to every day: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
