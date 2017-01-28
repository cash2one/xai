

#calss header
class _GENERIC():
	def __init__(self,): 
		self.name = "GENERIC"
		self.definitions = [u'shared by, typical of, or relating to a whole group of similar things, rather than to any particular thing: ', u'generic drugs or other products do not have a trademark and are sold without the name of the company that produced them']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
