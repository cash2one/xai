

#calss header
class _THROWAWAY():
	def __init__(self,): 
		self.name = "THROWAWAY"
		self.definitions = [u'made to be destroyed after use: ', u'something that someone says without thinking carefully and is not intended to be serious']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
