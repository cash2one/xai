

#calss header
class _HALTING():
	def __init__(self,): 
		self.name = "HALTING"
		self.definitions = [u'stopping often while you are saying or doing something, especially because you are nervous: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
