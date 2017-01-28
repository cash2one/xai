

#calss header
class _APPROACHABLE():
	def __init__(self,): 
		self.name = "APPROACHABLE"
		self.definitions = [u'friendly and easy to talk to: ', u'If a place is approachable, you can reach it or get near to it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
