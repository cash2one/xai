

#calss header
class _FIDUCIARY():
	def __init__(self,): 
		self.name = "FIDUCIARY"
		self.definitions = [u"relating to the responsibility to take care of someone else's money in a suitable way: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
