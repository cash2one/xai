

#calss header
class _UNTENABLE():
	def __init__(self,): 
		self.name = "UNTENABLE"
		self.definitions = [u'If a theory or argument is untenable, it cannot be supported or defended against criticism.', u'An untenable situation cannot continue as it is: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
