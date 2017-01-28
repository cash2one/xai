

#calss header
class _VIABLE():
	def __init__(self,): 
		self.name = "VIABLE"
		self.definitions = [u'able to work as intended or able to succeed: ', u'able to continue to exist as or develop into a living being: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
