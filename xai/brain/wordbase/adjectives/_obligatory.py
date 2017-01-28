

#calss header
class _OBLIGATORY():
	def __init__(self,): 
		self.name = "OBLIGATORY"
		self.definitions = [u'If something is obligatory, you must do it because of a rule or law, etc.: ', u'expected because it usually happens: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
