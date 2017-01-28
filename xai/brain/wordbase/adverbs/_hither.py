

#calss header
class _HITHER():
	def __init__(self,): 
		self.name = "HITHER"
		self.definitions = [u'to or towards this place: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
