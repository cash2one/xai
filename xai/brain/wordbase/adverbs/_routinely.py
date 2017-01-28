

#calss header
class _ROUTINELY():
	def __init__(self,): 
		self.name = "ROUTINELY"
		self.definitions = [u'used for describing what often or usually happens: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
