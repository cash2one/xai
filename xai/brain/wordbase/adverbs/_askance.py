

#calss header
class _ASKANCE():
	def __init__(self,): 
		self.name = "ASKANCE"
		self.definitions = [u'to look at or think about someone or something with doubt, disapproval, or no trust: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
