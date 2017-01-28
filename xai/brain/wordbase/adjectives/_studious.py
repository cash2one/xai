

#calss header
class _STUDIOUS():
	def __init__(self,): 
		self.name = "STUDIOUS"
		self.definitions = [u'A studious person enjoys studying or spends a lot of time studying: ', u'very careful or paying attention to all the small details: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
