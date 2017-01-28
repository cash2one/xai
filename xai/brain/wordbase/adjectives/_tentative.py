

#calss header
class _TENTATIVE():
	def __init__(self,): 
		self.name = "TENTATIVE"
		self.definitions = [u'(of a plan or idea) not certain or agreed, or (of a suggestion or action) said or done in a careful but uncertain way because you do not know if you are right: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
