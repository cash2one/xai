

#calss header
class _FORWARD():
	def __init__(self,): 
		self.name = "FORWARD"
		self.definitions = [u'towards the direction that is in front of you: ', u'relating to the future: ', u'confident and honest in a way that ignores the usual social rules and might seem rude: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
