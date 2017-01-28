

#calss header
class _UNSUITABLE():
	def __init__(self,): 
		self.name = "UNSUITABLE"
		self.definitions = [u'not acceptable or right for someone or something; not suitable: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
