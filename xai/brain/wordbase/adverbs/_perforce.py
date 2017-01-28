

#calss header
class _PERFORCE():
	def __init__(self,): 
		self.name = "PERFORCE"
		self.definitions = [u'because it is necessary']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
