

#calss header
class _LIVE():
	def __init__(self,): 
		self.name = "LIVE"
		self.definitions = [u'broadcast as it happens; performing or being performed in front of an audience: ', u'If a new system, especially a computer system, goes live, it starts to operate: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
