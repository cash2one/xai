

#calss header
class _WHATSOEVER():
	def __init__(self,): 
		self.name = "WHATSOEVER"
		self.definitions = [u'used after a negative phrase to add emphasis to the idea that is being expressed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
