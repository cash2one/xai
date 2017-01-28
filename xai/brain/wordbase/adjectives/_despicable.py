

#calss header
class _DESPICABLE():
	def __init__(self,): 
		self.name = "DESPICABLE"
		self.definitions = [u'very unpleasant or bad, causing strong feelings of dislike: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
