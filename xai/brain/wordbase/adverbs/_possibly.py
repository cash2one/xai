

#calss header
class _POSSIBLY():
	def __init__(self,): 
		self.name = "POSSIBLY"
		self.definitions = [u'used when something is not certain: ', u'used to agree or disagree when some doubt is involved: ', u'used with "can" or "could" for emphasis: ', u'used in polite requests: ', u'used when politely refusing offers: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
