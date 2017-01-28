

#calss header
class _UNDERSTANDABLE():
	def __init__(self,): 
		self.name = "UNDERSTANDABLE"
		self.definitions = [u'easy to understand: ', u"You say that something, for example someone's behaviour, is understandable, if you feel that it is usual and not strange or difficult to understand: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
