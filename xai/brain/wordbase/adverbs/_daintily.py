

#calss header
class _DAINTILY():
	def __init__(self,): 
		self.name = "DAINTILY"
		self.definitions = [u'in an attractive, careful way, especially used about something small or having small movements: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
