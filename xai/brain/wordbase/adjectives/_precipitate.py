

#calss header
class _PRECIPITATE():
	def __init__(self,): 
		self.name = "PRECIPITATE"
		self.definitions = [u'If an action is precipitate, it is done sooner or faster than expected and without enough thought or preparation: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
