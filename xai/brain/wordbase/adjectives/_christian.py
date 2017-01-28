

#calss header
class _CHRISTIAN():
	def __init__(self,): 
		self.name = "CHRISTIAN"
		self.definitions = [u'of or belonging to the religion based on the teachings of Jesus Christ: ', u'used to describe a person or action that is good, kind, helpful, etc.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
