

#calss header
class _INFATUATED():
	def __init__(self,): 
		self.name = "INFATUATED"
		self.definitions = [u'having a very strong but not usually lasting feeling of love or attraction for someone or something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
