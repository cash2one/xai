

#calss header
class _LOUSY():
	def __init__(self,): 
		self.name = "LOUSY"
		self.definitions = [u'very bad: ', u'used to say that you feel insulted by something: ', u'used to say that something is full of something, or has too much of it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
