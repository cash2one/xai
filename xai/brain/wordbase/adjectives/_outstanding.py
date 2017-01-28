

#calss header
class _OUTSTANDING():
	def __init__(self,): 
		self.name = "OUTSTANDING"
		self.definitions = [u'clearly very much better than what is usual: ', u'not yet paid, solved, or done: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
