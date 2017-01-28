

#calss header
class _QUINTESSENTIAL():
	def __init__(self,): 
		self.name = "QUINTESSENTIAL"
		self.definitions = [u'being the most typical example or most important part of something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
