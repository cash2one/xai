

#calss header
class _UNREADABLE():
	def __init__(self,): 
		self.name = "UNREADABLE"
		self.definitions = [u'too boring, complicated, or badly written to be worth reading: ', u'illegible (= impossible to read because not clear or untidy): ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
