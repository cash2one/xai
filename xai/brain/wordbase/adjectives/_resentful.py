

#calss header
class _RESENTFUL():
	def __init__(self,): 
		self.name = "RESENTFUL"
		self.definitions = [u'feeling angry because you have been forced to accept someone or something that you do not like: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
