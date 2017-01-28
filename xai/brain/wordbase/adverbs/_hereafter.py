

#calss header
class _HEREAFTER():
	def __init__(self,): 
		self.name = "HEREAFTER"
		self.definitions = [u'starting from this time; in the future: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
