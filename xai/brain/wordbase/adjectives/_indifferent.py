

#calss header
class _INDIFFERENT():
	def __init__(self,): 
		self.name = "INDIFFERENT"
		self.definitions = [u'not thinking about or interested in someone or something: ', u'not good, but not very bad: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
