

#calss header
class _ELIGIBLE():
	def __init__(self,): 
		self.name = "ELIGIBLE"
		self.definitions = [u'having the necessary qualities or satisfying the necessary conditions: ', u'An eligible person is not married and is thought to be a suitable future marriage partner, especially because they are rich and attractive: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
