

#calss header
class _FINELY():
	def __init__(self,): 
		self.name = "FINELY"
		self.definitions = [u'into very thin or small pieces: ', u'to an exact degree: ', u'beautifully: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
