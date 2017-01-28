

#calss header
class _INVALID():
	def __init__(self,): 
		self.name = "INVALID"
		self.definitions = [u'An invalid document, ticket, law, etc. is not legally or officially acceptable: ', u'An invalid opinion, argument, etc. is not correct, usually because it is not logical or not based on correct information: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
