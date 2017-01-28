

#calss header
class _SUPINE():
	def __init__(self,): 
		self.name = "SUPINE"
		self.definitions = [u'(lying) flat on your back, looking up: ', u'If you are supine, you are weak and willing to accept the control of others: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
