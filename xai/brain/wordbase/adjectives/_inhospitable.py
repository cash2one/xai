

#calss header
class _INHOSPITABLE():
	def __init__(self,): 
		self.name = "INHOSPITABLE"
		self.definitions = [u'not welcoming or generous to people who visit you: ', u'An inhospitable area is not suitable for humans to live in: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
