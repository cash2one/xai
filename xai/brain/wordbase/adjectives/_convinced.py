

#calss header
class _CONVINCED():
	def __init__(self,): 
		self.name = "CONVINCED"
		self.definitions = [u'certain: ', u'certain of your beliefs: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
