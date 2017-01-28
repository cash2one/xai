

#calss header
class _UNACCOUNTABLE():
	def __init__(self,): 
		self.name = "UNACCOUNTABLE"
		self.definitions = [u'to not be expected to explain or provide a reason to a particular person or organization for your actions: ', u'not able to be explained or understood: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
