

#calss header
class _EFFECTIVE():
	def __init__(self,): 
		self.name = "EFFECTIVE"
		self.definitions = [u'successful or achieving the results that you want: ', u'in fact, although not officially: ', u'If a law or rule becomes effective, it starts to be used: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
