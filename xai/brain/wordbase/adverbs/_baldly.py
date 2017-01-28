

#calss header
class _BALDLY():
	def __init__(self,): 
		self.name = "BALDLY"
		self.definitions = [u'in plain or basic language, without unnecessary words or details: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
