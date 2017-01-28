

#calss header
class _PRECARIOUSLY():
	def __init__(self,): 
		self.name = "PRECARIOUSLY"
		self.definitions = [u'in a way that is likely to fall, be damaged, fail, etc.: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
