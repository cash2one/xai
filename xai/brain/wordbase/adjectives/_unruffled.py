

#calss header
class _UNRUFFLED():
	def __init__(self,): 
		self.name = "UNRUFFLED"
		self.definitions = [u'calm; not nervous or worried, usually despite a difficult situation: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
