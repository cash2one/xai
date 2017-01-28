

#calss header
class _UNEARTHLY():
	def __init__(self,): 
		self.name = "UNEARTHLY"
		self.definitions = [u'An unearthly time is not at all convenient because it is too early in the morning or too late at night: ', u'strange in a mysterious and sometimes frightening way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
