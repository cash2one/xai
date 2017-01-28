

#calss header
class _STARCHY():
	def __init__(self,): 
		self.name = "STARCHY"
		self.definitions = [u'behaving in a formal way and without humour: ', u'containing a lot of starch: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
