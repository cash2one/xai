

#calss header
class _SLEEK():
	def __init__(self,): 
		self.name = "SLEEK"
		self.definitions = [u'(especially of hair, clothes, or shapes) smooth, shiny, and lying close to the body, and therefore looking well cared for; not untidy and with no parts sticking out: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
