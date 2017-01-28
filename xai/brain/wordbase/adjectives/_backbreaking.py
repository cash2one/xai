

#calss header
class _BACKBREAKING():
	def __init__(self,): 
		self.name = "BACKBREAKING"
		self.definitions = [u'needing a lot of hard, physical effort and making you feel extremely tired: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
