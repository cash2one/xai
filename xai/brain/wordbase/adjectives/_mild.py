

#calss header
class _MILD():
	def __init__(self,): 
		self.name = "MILD"
		self.definitions = [u'not violent, severe, or extreme: ', u'Mild weather is not very cold or not as cold as usual: ', u'used to describe food or a food flavour that is not very strong: ', u'gentle and calm: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
