

#calss header
class _PLAUSIBLE():
	def __init__(self,): 
		self.name = "PLAUSIBLE"
		self.definitions = [u'seeming likely to be true, or able to be believed: ', u'A plausible person appears to be honest and telling the truth, even if they are not: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
