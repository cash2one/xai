

#calss header
class _PRICKLY():
	def __init__(self,): 
		self.name = "PRICKLY"
		self.definitions = [u'covered with prickles: ', u'unfriendly and easily offended or annoyed: ', u'complicated and difficult to deal with: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
