

#calss header
class _SINFUL():
	def __init__(self,): 
		self.name = "SINFUL"
		self.definitions = [u'against the rules of a religion or morally wrong: ', u'used to refer to something that is very pleasant, but very bad for you: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
