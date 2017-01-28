

#calss header
class _QUICK():
	def __init__(self,): 
		self.name = "QUICK"
		self.definitions = [u'happening or done with great speed, or lasting only a short time: ', u'doing something fast: ', u'to do something fast, sometimes too fast: ', u'used to describe someone who is clever and understands or notices things quickly: ', u'someone who is able to learn things quickly: ', u'produced quickly and therefore not perfect: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
