

#calss header
class _ROUGH():
	def __init__(self,): 
		self.name = "ROUGH"
		self.definitions = [u'forcefully or violently: ', u'to live outside not in a house, and sleep on the ground: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
