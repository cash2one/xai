

#calss header
class _ELEVATED():
	def __init__(self,): 
		self.name = "ELEVATED"
		self.definitions = [u'raised: ', u'high or important: ', u'greater than is normal or reasonable: ', u'formal or typical of language found in literature: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
