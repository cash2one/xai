

#calss header
class _EASY():
	def __init__(self,): 
		self.name = "EASY"
		self.definitions = [u'needing little effort: ', u'comfortable or calm; free from worry, pain, etc.: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
