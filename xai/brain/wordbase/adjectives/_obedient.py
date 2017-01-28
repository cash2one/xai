

#calss header
class _OBEDIENT():
	def __init__(self,): 
		self.name = "OBEDIENT"
		self.definitions = [u'doing, or willing to do, what you have been told to do by someone in authority: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
