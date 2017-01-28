

#calss header
class _INDECISIVE():
	def __init__(self,): 
		self.name = "INDECISIVE"
		self.definitions = [u'not good at making decisions: ', u'not having a clear meaning or producing a decision']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
