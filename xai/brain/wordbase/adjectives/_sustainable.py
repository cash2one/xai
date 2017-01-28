

#calss header
class _SUSTAINABLE():
	def __init__(self,): 
		self.name = "SUSTAINABLE"
		self.definitions = [u'able to continue over a period of time: ', u'causing little or no damage to the environment and therefore able to continue for a long time: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
