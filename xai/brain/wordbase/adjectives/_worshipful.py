

#calss header
class _WORSHIPFUL():
	def __init__(self,): 
		self.name = "WORSHIPFUL"
		self.definitions = [u'giving someone or something great respect or admiration', u'used in the title of societies of skilled workers or some important officials: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
