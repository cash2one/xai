

#calss header
class _CONNECTED():
	def __init__(self,): 
		self.name = "CONNECTED"
		self.definitions = [u'joined together: ', u'related to someone or something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
