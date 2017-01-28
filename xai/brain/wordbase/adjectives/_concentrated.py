

#calss header
class _CONCENTRATED():
	def __init__(self,): 
		self.name = "CONCENTRATED"
		self.definitions = [u'using a lot of effort to succeed at one particular thing: ', u'having had some liquid removed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
