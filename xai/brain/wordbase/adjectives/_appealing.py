

#calss header
class _APPEALING():
	def __init__(self,): 
		self.name = "APPEALING"
		self.definitions = [u'attractive or interesting: ', u'showing that you want people to help or protect you: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
