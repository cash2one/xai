

#calss header
class _ACCOMPANYING():
	def __init__(self,): 
		self.name = "ACCOMPANYING"
		self.definitions = [u'appearing or going with someone or something else: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
