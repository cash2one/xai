

#calss header
class _QUIRKY():
	def __init__(self,): 
		self.name = "QUIRKY"
		self.definitions = [u'unusual in an attractive and interesting way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
