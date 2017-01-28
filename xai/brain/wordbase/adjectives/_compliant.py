

#calss header
class _COMPLIANT():
	def __init__(self,): 
		self.name = "COMPLIANT"
		self.definitions = [u'willing to do what other people want you to do: ', u'used to describe something that obeys a particular rule or law: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
