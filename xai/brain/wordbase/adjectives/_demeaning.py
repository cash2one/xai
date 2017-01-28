

#calss header
class _DEMEANING():
	def __init__(self,): 
		self.name = "DEMEANING"
		self.definitions = [u'causing someone to become or feel less respected: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
