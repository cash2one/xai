

#calss header
class _ENOUGH():
	def __init__(self,): 
		self.name = "ENOUGH"
		self.definitions = [u'used after an adjective, adverb, or verb to mean to the necessary degree: ', u'used after an adjective or adverb to mean quite: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
