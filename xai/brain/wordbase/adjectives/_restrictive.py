

#calss header
class _RESTRICTIVE():
	def __init__(self,): 
		self.name = "RESTRICTIVE"
		self.definitions = [u'limiting the freedom of someone or preventing something from growing: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
