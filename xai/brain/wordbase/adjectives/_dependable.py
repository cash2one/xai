

#calss header
class _DEPENDABLE():
	def __init__(self,): 
		self.name = "DEPENDABLE"
		self.definitions = [u'If someone or something is dependable, you can have confidence in him, her, or it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
