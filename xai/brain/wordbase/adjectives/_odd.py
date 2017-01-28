

#calss header
class _ODD():
	def __init__(self,): 
		self.name = "ODD"
		self.definitions = [u'strange or unexpected: ', u'not happening often: ', u'(of numbers) not able to be divided exactly by two: ', u'(of something that should be in a pair or set) separated from its pair or set: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
