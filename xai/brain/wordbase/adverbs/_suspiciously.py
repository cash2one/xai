

#calss header
class _SUSPICIOUSLY():
	def __init__(self,): 
		self.name = "SUSPICIOUSLY"
		self.definitions = [u'in a way that makes you think that something is wrong: ', u'in a way that makes you think someone is guilty of something wrong or illegal: ', u'in a way that makes you think something may be true: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
