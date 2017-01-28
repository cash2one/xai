

#calss header
class _EQUALLY():
	def __init__(self,): 
		self.name = "EQUALLY"
		self.definitions = [u'fairly and in the same way: ', u'in equal amounts: ', u'to the same degree: ', u'used for adding an idea that is as important as what you have just said: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
