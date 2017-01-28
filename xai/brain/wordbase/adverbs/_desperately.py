

#calss header
class _DESPERATELY():
	def __init__(self,): 
		self.name = "DESPERATELY"
		self.definitions = [u'extremely or very much: ', u'in a way that shows you are frightened and ready to try anything to change a situation: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
