

#calss header
class _FORGIVING():
	def __init__(self,): 
		self.name = "FORGIVING"
		self.definitions = [u'willing to forgive: ', u'Something that is forgiving allows you to make mistakes or allows for your weaknesses: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
