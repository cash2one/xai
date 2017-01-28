

#calss header
class _SORDID():
	def __init__(self,): 
		self.name = "SORDID"
		self.definitions = [u'dirty and unpleasant: ', u'morally wrong and shocking: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
