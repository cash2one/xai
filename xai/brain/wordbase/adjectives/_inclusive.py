

#calss header
class _INCLUSIVE():
	def __init__(self,): 
		self.name = "INCLUSIVE"
		self.definitions = [u'An inclusive price or amount includes everything: ', u'including the first and last date or number stated: ', u'An inclusive group or organization tries to include many different types of people and treat them all fairly and equally: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
