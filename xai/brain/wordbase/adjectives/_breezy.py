

#calss header
class _BREEZY():
	def __init__(self,): 
		self.name = "BREEZY"
		self.definitions = [u'with wind that is quite strong but pleasant: ', u'happy, confident, and enthusiastic: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
