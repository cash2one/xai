

#calss header
class _DECOROUS():
	def __init__(self,): 
		self.name = "DECOROUS"
		self.definitions = [u'behaving politely and in a controlled way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
