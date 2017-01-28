

#calss header
class _DIFFERENT():
	def __init__(self,): 
		self.name = "DIFFERENT"
		self.definitions = [u'not the same: ', u'used when you think someone or something is unusual or shows bad judgment: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
