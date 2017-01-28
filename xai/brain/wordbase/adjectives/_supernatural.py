

#calss header
class _SUPERNATURAL():
	def __init__(self,): 
		self.name = "SUPERNATURAL"
		self.definitions = [u'caused by forces that cannot be explained by science: ', u'things that cannot be explained by science: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
