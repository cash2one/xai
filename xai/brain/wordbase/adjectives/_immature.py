

#calss header
class _IMMATURE():
	def __init__(self,): 
		self.name = "IMMATURE"
		self.definitions = [u'not behaving in a way that is as calm and wise as people expect from someone of your age: ', u'not having much experience of something: ', u'not yet completely grown or developed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
