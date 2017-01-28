

#calss header
class _UNGUARDED():
	def __init__(self,): 
		self.name = "UNGUARDED"
		self.definitions = [u'not guarded or protected: ', u'If you make an unguarded remark or say something in an unguarded moment, you tell someone something that you would usually keep secret, sometimes in a way that shows bad judgment: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
