

#calss header
class _WOODWIND():
	def __init__(self,): 
		self.name = "WOODWIND"
		self.definitions = [u'belonging or relating to a group of pipe-shaped musical instruments that are played by blowing through one end or across a hole near one end: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
