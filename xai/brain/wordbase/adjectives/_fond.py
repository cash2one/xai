

#calss header
class _FOND():
	def __init__(self,): 
		self.name = "FOND"
		self.definitions = [u'to like someone or something very much; to like doing something: ', u'happy and loving: ', u'something that you would like to be true but that is probably not: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
