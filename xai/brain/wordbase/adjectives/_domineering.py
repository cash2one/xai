

#calss header
class _DOMINEERING():
	def __init__(self,): 
		self.name = "DOMINEERING"
		self.definitions = [u'trying to control other people without thinking about their feelings: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
