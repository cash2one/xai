

#calss header
class _ATROCIOUS():
	def __init__(self,): 
		self.name = "ATROCIOUS"
		self.definitions = [u'of very bad quality: ', u'violent and shocking: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
