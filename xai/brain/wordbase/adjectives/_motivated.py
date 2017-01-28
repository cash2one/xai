

#calss header
class _MOTIVATED():
	def __init__(self,): 
		self.name = "MOTIVATED"
		self.definitions = [u'very enthusiastic or determined because you really want to do something: ', u'having a particular motive (= a reason for behaviour): ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
