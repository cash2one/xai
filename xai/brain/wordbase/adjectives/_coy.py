

#calss header
class _COY():
	def __init__(self,): 
		self.name = "COY"
		self.definitions = [u'intentionally keeping something secret: ', u'(especially of women) being or pretending to be shy, or like a child: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
