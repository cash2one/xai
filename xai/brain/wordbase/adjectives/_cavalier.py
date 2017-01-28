

#calss header
class _CAVALIER():
	def __init__(self,): 
		self.name = "CAVALIER"
		self.definitions = [u"not considering other people's feelings or safety: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
