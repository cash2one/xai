

#calss header
class _DORMANT():
	def __init__(self,): 
		self.name = "DORMANT"
		self.definitions = [u'Something that is dormant is not active or growing but has the ability to be active at a later time: ', u'If something lies dormant, it is not active: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
