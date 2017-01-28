

#calss header
class _STIFFLY():
	def __init__(self,): 
		self.name = "STIFFLY"
		self.definitions = [u'straight and not bending: ', u'in a way that is too formal: ', u'severely: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
