

#calss header
class _UNSUITED():
	def __init__(self,): 
		self.name = "UNSUITED"
		self.definitions = [u'not right for someone or something, usually in character: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
