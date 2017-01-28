

#calss header
class _SURELY():
	def __init__(self,): 
		self.name = "SURELY"
		self.definitions = [u'used to express that you are certain or almost certain about something: ', u'used to express surprise that something has happened or is going to happen: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
