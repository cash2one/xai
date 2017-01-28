

#calss header
class _NORMALLY():
	def __init__(self,): 
		self.name = "NORMALLY"
		self.definitions = [u'If something happens normally, it happens in the usual or expected way: ', u'If you normally do something, you usually or regularly do it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
