

#calss header
class _DIVISIVE():
	def __init__(self,): 
		self.name = "DIVISIVE"
		self.definitions = [u'used to describe something that causes great and sometimes unfriendly disagreement within a group of people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
