

#calss header
class _ABSOLUTELY():
	def __init__(self,): 
		self.name = "ABSOLUTELY"
		self.definitions = [u'completely: ', u'used for adding force to a strong adjective that is not usually used with "very" or to a verb expressing strong emotion: ', u'used as a strong way of saying "yes": ', u'used as a strong way of saying "no": ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
