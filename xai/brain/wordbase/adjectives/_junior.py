

#calss header
class _JUNIOR():
	def __init__(self,): 
		self.name = "JUNIOR"
		self.definitions = [u'low or lower in rank: ', u'connected with or involving young people below a particular age: ', u"used after a man's name to refer to the younger of two men in the same family who have the same name: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
