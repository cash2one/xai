

#calss header
class _ADOLESCENT():
	def __init__(self,): 
		self.name = "ADOLESCENT"
		self.definitions = [u'being or relating to an adolescent: ', u"used to describe an adult or an adult's behaviour that is silly and like a child's: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
