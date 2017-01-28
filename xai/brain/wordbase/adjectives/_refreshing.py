

#calss header
class _REFRESHING():
	def __init__(self,): 
		self.name = "REFRESHING"
		self.definitions = [u'making you feel less hot or tired: ', u'pleasantly different and interesting: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
