

#calss header
class _UNFAMILIAR():
	def __init__(self,): 
		self.name = "UNFAMILIAR"
		self.definitions = [u'not known to you: ', u'to not have any knowledge or experience of something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
