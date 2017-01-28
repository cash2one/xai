

#calss header
class _PERHAPS():
	def __init__(self,): 
		self.name = "PERHAPS"
		self.definitions = [u'used to show that something is possible or that you are not certain about something: ', u'used to show that a number or amount is approximate: ', u'used when making polite requests or statements of opinion: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
