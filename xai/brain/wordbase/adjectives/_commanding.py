

#calss header
class _COMMANDING():
	def __init__(self,): 
		self.name = "COMMANDING"
		self.definitions = [u'having the authority to give orders: ', u'A commanding voice or manner seems to have authority and therefore demands your attention: ', u'in a very successful position and likely to win or succeed: ', u'a position or view from which a lot of land can be seen: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
