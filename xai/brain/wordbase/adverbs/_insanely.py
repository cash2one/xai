

#calss header
class _INSANELY():
	def __init__(self,): 
		self.name = "INSANELY"
		self.definitions = [u'extremely and unreasonably: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
