

#calss header
class _ALMIGHTY():
	def __init__(self,): 
		self.name = "ALMIGHTY"
		self.definitions = [u'(of God) having the power to do everything: ', u'very big, loud, or serious: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
