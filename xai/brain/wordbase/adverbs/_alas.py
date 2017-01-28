

#calss header
class _ALAS():
	def __init__(self,): 
		self.name = "ALAS"
		self.definitions = [u'used to express sadness or feeling sorry about something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
