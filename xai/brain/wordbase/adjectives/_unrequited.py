

#calss header
class _UNREQUITED():
	def __init__(self,): 
		self.name = "UNREQUITED"
		self.definitions = [u'If love that you feel for someone is unrequited, it is not felt in the same way by the other person: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
