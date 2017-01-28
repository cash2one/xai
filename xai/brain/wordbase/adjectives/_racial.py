

#calss header
class _RACIAL():
	def __init__(self,): 
		self.name = "RACIAL"
		self.definitions = [u'happening between people of different races: ', u"connected with someone's race: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
