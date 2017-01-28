

#calss header
class _DEHYDRATED():
	def __init__(self,): 
		self.name = "DEHYDRATED"
		self.definitions = [u'not having the normal amount of water in your body so that you feel ill or weak']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
