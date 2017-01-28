

#calss header
class _SINGLE():
	def __init__(self,): 
		self.name = "SINGLE"
		self.definitions = [u'one only: ', u'not married, or not having a romantic relationship with someone: ', u'considered on its own and separate from other things: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
