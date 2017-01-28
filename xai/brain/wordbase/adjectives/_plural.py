

#calss header
class _PLURAL():
	def __init__(self,): 
		self.name = "PLURAL"
		self.definitions = [u'consisting of lots of different races or types of people or of different things: ', u'for or relating to more than one person or thing: ', u'of or relating to the form that expresses more than one: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
