

#calss header
class _MANGY():
	def __init__(self,): 
		self.name = "MANGY"
		self.definitions = [u'suffering from mange: ', u'used to describe something that is old and dirty and has been used a lot: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
