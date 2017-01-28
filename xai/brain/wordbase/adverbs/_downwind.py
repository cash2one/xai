

#calss header
class _DOWNWIND():
	def __init__(self,): 
		self.name = "DOWNWIND"
		self.definitions = [u'in the direction in which the wind blows; with the wind behind: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
