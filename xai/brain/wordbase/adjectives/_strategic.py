

#calss header
class _STRATEGIC():
	def __init__(self,): 
		self.name = "STRATEGIC"
		self.definitions = [u'helping to achieve a plan, for example in business or politics: ', u'used to provide military forces with an advantage: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
