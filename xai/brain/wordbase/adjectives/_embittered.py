

#calss header
class _EMBITTERED():
	def __init__(self,): 
		self.name = "EMBITTERED"
		self.definitions = [u'very angry about unfair things that have happened to you: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
