

#calss header
class _ABSENTLY():
	def __init__(self,): 
		self.name = "ABSENTLY"
		self.definitions = [u'as if you are not paying attention to what is happening near you, and are thinking about other things: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
