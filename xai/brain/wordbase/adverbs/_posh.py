

#calss header
class _POSH():
	def __init__(self,): 
		self.name = "POSH"
		self.definitions = [u'as though from a high social class: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
