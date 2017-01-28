

#calss header
class _DARLING():
	def __init__(self,): 
		self.name = "DARLING"
		self.definitions = [u'used when talking to someone you love, for example in a letter, to say that you love them very much: ', u'very attractive: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
