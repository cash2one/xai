

#calss header
class _IMPERATIVE():
	def __init__(self,): 
		self.name = "IMPERATIVE"
		self.definitions = [u'extremely important or urgent: ', u'used to describe the form of a verb that is usually used for giving orders: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
