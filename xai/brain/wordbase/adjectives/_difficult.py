

#calss header
class _DIFFICULT():
	def __init__(self,): 
		self.name = "DIFFICULT"
		self.definitions = [u'needing skill or effort: ', u'not friendly, easy to deal with, or behaving well: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
