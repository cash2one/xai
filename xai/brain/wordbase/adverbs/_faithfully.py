

#calss header
class _FAITHFULLY():
	def __init__(self,): 
		self.name = "FAITHFULLY"
		self.definitions = [u'in a loyal way or a way that can be trusted: ', u'used at the end of a formal letter beginning with "Dear Sir" or "Dear Madam"', u'in a way that is true or accurate: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
