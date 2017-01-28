

#calss header
class _MIFFED():
	def __init__(self,): 
		self.name = "MIFFED"
		self.definitions = [u"annoyed at someone's behaviour towards you: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
