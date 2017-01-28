

#calss header
class _ILLIBERAL():
	def __init__(self,): 
		self.name = "ILLIBERAL"
		self.definitions = [u'limiting freedom of expression, thought, behaviour, etc.: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
