

#calss header
class _AWFULLY():
	def __init__(self,): 
		self.name = "AWFULLY"
		self.definitions = [u'very or extremely, when used before an adjective or adverb: ', u'extremely badly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
