

#calss header
class _NAMELY():
	def __init__(self,): 
		self.name = "NAMELY"
		self.definitions = [u'used when you want to give more detail or be more exact about something you have just said: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
