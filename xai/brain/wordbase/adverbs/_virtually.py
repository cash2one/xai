

#calss header
class _VIRTUALLY():
	def __init__(self,): 
		self.name = "VIRTUALLY"
		self.definitions = [u'almost: ', u'using a computer to do or see something instead of going to a place or talking to a person: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
