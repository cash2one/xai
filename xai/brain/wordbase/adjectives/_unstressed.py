

#calss header
class _UNSTRESSED():
	def __init__(self,): 
		self.name = "UNSTRESSED"
		self.definitions = [u'not feeling worried; feeling relaxed and not experiencing stress: ', u'(of a word or syllable) not pronounced with stress (= emphasis) : ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
